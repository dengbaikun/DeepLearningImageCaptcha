import io

import torch
from PIL import Image
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms

from model import CNN
import numpy as np
import torch
from torch.autograd import Variable
import setting
import dataset
from model import CNN
import encoding
import requests
transform = transforms.Compose([
    # transforms.ColorJitter(),
    transforms.Grayscale(),
    transforms.ToTensor(),
    # transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])


class mydataset(Dataset):

    def __init__(self, image, transform=None):
        self.transform = transform
        self.image = image

    def __len__(self):
        return 1

    def __getitem__(self, idx):
        if self.transform is not None:
            image = self.transform(self.image)
        return image


def ocr_captcha(image):
    cnn = CNN()
    cnn.eval()
    cnn.load_state_dict(torch.load('cpu-model-5.pkl'))
    print("load cnn net.")
    dataset = mydataset(image, transform=transform)
    eval_dataloader = DataLoader(dataset, batch_size=1, shuffle=True)
    for i, (images) in enumerate(eval_dataloader):
        vimage = Variable(images)
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
        print(f"predict_label={predict_label}")
    return predict_label

def req_img():

    headers = {
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Proxy-Connection": "keep-alive",
        "Referer": "http://192.168.148.1:7777/login.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    cookies = {
        "_ga": "GA1.1.1087465725.1662016060"
    }
    url = "http://192.168.148.1:7777/code/getKaptChaCode"
    params = {
        "timestamp": "1690273207979"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params, verify=False)

    return response.content



if __name__ == '__main__':
    # img_root = "D:/data/t1/00NN_1bcc6e2b1a4d4e0a9fcf053bf154a7f3.png"
    # with open(img_root, 'rb') as f:
    #     img_bytes = f.read()
    image = Image.open(io.BytesIO(req_img()))
    image = image.resize((160, 60))
    res = ocr_captcha(image)
    print(f"res={res}")
