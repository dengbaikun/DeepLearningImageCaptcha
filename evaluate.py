# -*- coding: UTF-8 -*-
import numpy as np
import torch
from torch.autograd import Variable
import setting
import dataset
from model import CNN
import encoding


def main():
    cnn = CNN()
    if torch.cuda.is_available():
        cnn = CNN().cuda()
    cnn.eval()
    cnn.load_state_dict(torch.load('model.pkl'))
    print("load cnn net.")

    eval_dataloader = dataset.get_eval_data_loader()

    correct = 0
    total = 0
    for i, (images, labels) in enumerate(eval_dataloader):
        if torch.cuda.is_available():
            images = images.cuda()
            labels = labels.cuda()
        image = images
        vimage = Variable(image)
        predict_label = cnn(vimage)

        c0 = setting.ALL_CHAR_SET[np.argmax(
            predict_label[0, 0:setting.ALL_CHAR_SET_LEN].data.cpu().numpy())]
        c1 = setting.ALL_CHAR_SET[np.argmax(
            predict_label[0, setting.ALL_CHAR_SET_LEN:2 * setting.ALL_CHAR_SET_LEN].data.cpu().numpy())]
        c2 = setting.ALL_CHAR_SET[np.argmax(
            predict_label[0, 2 * setting.ALL_CHAR_SET_LEN:3 * setting.ALL_CHAR_SET_LEN].data.cpu().numpy())]
        c3 = setting.ALL_CHAR_SET[np.argmax(
            predict_label[0, 3 * setting.ALL_CHAR_SET_LEN:4 * setting.ALL_CHAR_SET_LEN].data.cpu().numpy())]
        predict_label = '%s%s%s%s' % (c0, c1, c2, c3)
        true_label = encoding.decode(labels.cpu().numpy()[0])
        total += labels.size(0)
        if (predict_label == true_label):
            correct += 1
        if (total % 200 == 0):
            print('Test Accuracy of the model on the %d eval images: %f %%' %
                  (total, 100 * correct / total))
    print('Test Accuracy of the model on the %d eval images: %f %%' %
          (total, 100 * correct / total))
    return correct / total


if __name__ == '__main__':
    main()
