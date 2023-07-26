深度学习识别验证码
=========

Origin Repo: [https://github.com/dee1024/pytorch-captcha-recognition](https://github.com/dee1024/pytorch-captcha-recognition).

本项目致力于使用神经网络来识别各种验证码。

特性
===
- __端到端，不需要做更多的图片预处理（比如图片字符切割、图片尺寸归一化、图片字符标记、字符图片特征提取）__
- __验证码包括数字、大写字母、小写__
- __采用自己生成的验证码来作为神经网络的训练集合、测试集合、预测集合__
- __纯四位数字，验证码识别率高达 99.9999 %__
- __四位数字 + 大写字符，验证码识别率约 96 %__
- __深度学习框架pytorch + 验证码生成器ImageCaptcha__


原理
===

- __训练集合生成__

    使用常用的 Python 验证码生成库 ImageCaptcha，生成 10w 个验证码，并且都自动标记好;
    如果需要识别其他的验证码也同样的道理，寻找对应的验证码生成算法自动生成已经标记好的训练集合或者手动对标记，需要上万级别的数量，纯手工需要一定的时间，再或者可以借助一些网络的打码平台进行标记

- __训练卷积神经网络__
    构建一个多层的卷积网络，进行多标签分类模型的训练
    标记的每个字符都做 one-hot 编码
    批量输入图片集合和标记数据，大概15个Epoch后，准确率已经达到 96% 以上


验证码识别率展示
========
![](https://raw.githubusercontent.com/dee1024/pytorch-captcha-recognition/master/docs/number.png)
![](https://raw.githubusercontent.com/dee1024/pytorch-captcha-recognition/master/docs/number2.png)


快速开始
====
- __步骤一：10分钟环境安装__

    Python3.5+ 、ImageCaptcha库(pip install captcha)、 Pytorch(参考官网http://pytorch.org)


- __步骤二：生成验证码__
    ```bash
    python generate.py
    ```
    执行以上命令，会在目录 dataset/train/ 下生成多张验证码图片，图片已经标注好，数量可以是 1w、5w、10w，通过 captcha-gen.py 内的 count 参数设定
    
- __步骤三：训练模型__
    ```bash
    python train.py
    ```
    使用步骤一生成的验证码图集合用CNN模型（在 catcha_cnn_model 中定义）进行训练，训练完成会生成文件 model.pkl

- __步骤四：测试模型__
    ```bash
    python test.py
    ```
    可以在控制台，看到模型的准确率（如 95%） ，如果准确率较低，回到步骤一，生成更多的图片集合再次训练

- __步骤五：使用模型做预测__
    ```bash
    python predict.py
    ```
    可以在控制台，看到预测输出的结果
    
作者
===
* __Dee Qiu__ <coolcooldee@gmail.com>
* __Germey__ <cqc@cuiqingcai.com>


修改了训练准确率可以达到98%
而且采用cuda训练模型,改了大小写
```
epoch: 60 step: 9 loss: 0.009964840486645699
epoch: 60 step: 19 loss: 0.00986679457128048
epoch: 60 step: 29 loss: 0.010375024750828743
epoch: 60 step: 39 loss: 0.010238828137516975
epoch: 60 step: 49 loss: 0.010021325200796127
epoch: 60 step: 59 loss: 0.010487931780517101
epoch: 60 step: 69 loss: 0.010111748240888119
epoch: 60 step: 79 loss: 0.010158763267099857
epoch: 60 step: 89 loss: 0.010008592158555984
epoch: 60 step: 99 loss: 0.010192733258008957
save model
epoch: 60 step: 109 loss: 0.010224193334579468
epoch: 60 step: 119 loss: 0.009969135746359825
epoch: 60 step: 129 loss: 0.01000596396625042
epoch: 60 step: 139 loss: 0.0101090082898736
epoch: 60 step: 149 loss: 0.00997310783714056
epoch: 60 step: 159 loss: 0.010136067867279053
epoch: 60 step: 169 loss: 0.01040852814912796
epoch: 60 step: 179 loss: 0.010031051933765411
epoch: 60 step: 189 loss: 0.010585060343146324
epoch: 60 step: 195 loss: 0.01018571387976408
load cnn net.
Test Accuracy of the model on the 200 eval images: 97.000000 %
Test Accuracy of the model on the 400 eval images: 97.750000 %
Test Accuracy of the model on the 600 eval images: 98.166667 %
Test Accuracy of the model on the 800 eval images: 98.625000 %
Test Accuracy of the model on the 1000 eval images: 98.700000 %
Test Accuracy of the model on the 1200 eval images: 98.750000 %
Test Accuracy of the model on the 1400 eval images: 98.571429 %
Test Accuracy of the model on the 1600 eval images: 98.562500 %
Test Accuracy of the model on the 1800 eval images: 98.555556 %
Test Accuracy of the model on the 2000 eval images: 98.600000 %
Test Accuracy of the model on the 2200 eval images: 98.636364 %
Test Accuracy of the model on the 2400 eval images: 98.625000 %
Test Accuracy of the model on the 2600 eval images: 98.692308 %
Test Accuracy of the model on the 2800 eval images: 98.785714 %
Test Accuracy of the model on the 3000 eval images: 98.666667 %
Test Accuracy of the model on the 3200 eval images: 98.593750 %
Test Accuracy of the model on the 3400 eval images: 98.411765 %
Test Accuracy of the model on the 3600 eval images: 98.444444 %
Test Accuracy of the model on the 3800 eval images: 98.447368 %
Test Accuracy of the model on the 4000 eval images: 98.475000 %
Test Accuracy of the model on the 4200 eval images: 98.476190 %
Test Accuracy of the model on the 4400 eval images: 98.409091 %
Test Accuracy of the model on the 4600 eval images: 98.369565 %
Test Accuracy of the model on the 4800 eval images: 98.333333 %
Test Accuracy of the model on the 5000 eval images: 98.340000 %
Test Accuracy of the model on the 5200 eval images: 98.326923 %
Test Accuracy of the model on the 5400 eval images: 98.351852 %
Test Accuracy of the model on the 5600 eval images: 98.375000 %
Test Accuracy of the model on the 5800 eval images: 98.396552 %
Test Accuracy of the model on the 6000 eval images: 98.383333 %
Test Accuracy of the model on the 6200 eval images: 98.403226 %
Test Accuracy of the model on the 6400 eval images: 98.375000 %
Test Accuracy of the model on the 6600 eval images: 98.318182 %
Test Accuracy of the model on the 6800 eval images: 98.352941 %
Test Accuracy of the model on the 7000 eval images: 98.371429 %
Test Accuracy of the model on the 7200 eval images: 98.347222 %
Test Accuracy of the model on the 7400 eval images: 98.378378 %
Test Accuracy of the model on the 7600 eval images: 98.381579 %
Test Accuracy of the model on the 7800 eval images: 98.410256 %
Test Accuracy of the model on the 8000 eval images: 98.412500 %
Test Accuracy of the model on the 8200 eval images: 98.414634 %
Test Accuracy of the model on the 8400 eval images: 98.392857 %
Test Accuracy of the model on the 8600 eval images: 98.406977 %
Test Accuracy of the model on the 8800 eval images: 98.386364 %
Test Accuracy of the model on the 9000 eval images: 98.411111 %
Test Accuracy of the model on the 9200 eval images: 98.380435 %
Test Accuracy of the model on the 9400 eval images: 98.404255 %
Test Accuracy of the model on the 9600 eval images: 98.416667 %
Test Accuracy of the model on the 9800 eval images: 98.428571 %
Test Accuracy of the model on the 10000 eval images: 98.420000 %
Test Accuracy of the model on the 10000 eval images: 98.420000 %
```