# -*- coding: UTF-8 -*-
import torch
import torch.nn as nn
from matplotlib import pyplot as plt
from torch.autograd import Variable
import dataset
from model import CNN
from evaluate import main as evaluate

num_epochs = 100
batch_size = 100000
learning_rate = 0.0001


def main():
    cnn = CNN()
    if torch.cuda.is_available():
        cnn = CNN().cuda()
    cnn.train()

    criterion = nn.MultiLabelSoftMarginLoss().cuda()
    optimizer = torch.optim.Adam(cnn.parameters(), lr=learning_rate)
    max_eval_acc = -1

    train_dataloader = dataset.get_train_data_loader()
    epoch_list = []
    loss_list = []
    plt.ion()
    for epoch in range(num_epochs):
        if epoch == 0:
            plt.pause(10)  # 启动时间，方便截屏
        for i, (images, labels) in enumerate(train_dataloader):
            if torch.cuda.is_available():
                images = images.cuda()
                labels = labels.cuda()
            images = Variable(images)
            labels = Variable(labels.float())
            predict_labels = cnn(images)
            loss = criterion(predict_labels, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            if (i + 1) % 10 == 0:
                print("epoch:", epoch, "step:", i, "loss:", loss.item())
            if (i + 1) % 100 == 0:
                # current is model.pkl
                torch.save(cnn.state_dict(), "./model.pkl")
                print("save model")
        epoch_list.append(epoch)
        loss_list.append(loss.item())
        plt.title("loss")
        plt.plot(epoch_list, loss_list)
        plt.xlabel("epoch")
        plt.ylabel("loss")
        plt.pause(0.5)
        print("epoch:", epoch, "step:", i, "loss:", loss.item())
        eval_acc = evaluate()
        if eval_acc > max_eval_acc:
            # best model save as best_model.pkl
            torch.save(cnn.state_dict(), "./best_model.pkl")
            max_eval_acc = eval_acc
            print("save best model")
    torch.save(cnn.state_dict(), "./model.pkl")
    plt.ioff()
    plt.show()
    print("save last model")


if __name__ == '__main__':
    main()
