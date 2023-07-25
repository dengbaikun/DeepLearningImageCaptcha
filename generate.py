# -*- coding: UTF-8 -*-
import multiprocessing
import uuid
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process

from captcha.image import ImageCaptcha  # pip install captcha
from PIL import Image
import random
import time
import setting
import os


def generate_captcha_text():
    captcha_text = []
    for i in range(setting.MAX_CAPTCHA):
        c = random.choice(setting.ALL_CHAR_SET)
        captcha_text.append(c)
    return ''.join(captcha_text)


def generate_captcha_text_and_image():
    image = ImageCaptcha()
    captcha_text = generate_captcha_text()
    captcha_image = Image.open(image.generate(captcha_text))
    return captcha_text, captcha_image


def get_uuid():
    get_timestamp_uuid = uuid.uuid1()  # 根据 时间戳生成 uuid , 保证全球唯一
    return str(get_timestamp_uuid).replace("-", "")


def gen_image(gen_path, gen_count):
    # gen_path=gen_params[0]
    # gen_count=gen_params[1]
    for i in range(gen_count):
        # now = str(int(time.time()))
        text, image = generate_captcha_text_and_image()
        filename = text + '_' + get_uuid() + '.png'
        image.save(gen_path + os.path.sep + filename)
    print("1000")


if __name__ == '__main__':

    count = 1000
    path = setting.TRAIN_DATASET_PATH
    if not os.path.exists(path):
        os.makedirs(path)
    thread = []
    future_count = 100
    l_count = int(count / future_count)
    pool = multiprocessing.Pool()
    gen_params = [(path, l_count) for i in range(future_count)]
    pool.starmap(gen_image, gen_params)
    pool.close()
    pool.join()
    # print('saved %d : %s' % (i + 1, filename))
