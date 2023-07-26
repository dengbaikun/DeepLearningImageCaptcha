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
save best model
epoch: 43 step: 9 loss: 0.010866313241422176
epoch: 43 step: 19 loss: 0.01089353859424591
epoch: 43 step: 29 loss: 0.01080146711319685
epoch: 43 step: 39 loss: 0.010517042130231857
epoch: 43 step: 49 loss: 0.01082000881433487
epoch: 43 step: 59 loss: 0.010554435662925243
epoch: 43 step: 69 loss: 0.011080639436841011
epoch: 43 step: 79 loss: 0.010639272630214691
epoch: 43 step: 89 loss: 0.010714512318372726
epoch: 43 step: 99 loss: 0.010591348633170128
save model
epoch: 43 step: 109 loss: 0.010973664000630379
epoch: 43 step: 119 loss: 0.010775553993880749
epoch: 43 step: 129 loss: 0.010660551488399506
epoch: 43 step: 139 loss: 0.010809225030243397
epoch: 43 step: 149 loss: 0.010678241029381752
epoch: 43 step: 159 loss: 0.010679996572434902
epoch: 43 step: 169 loss: 0.01073421724140644
epoch: 43 step: 179 loss: 0.010784017853438854
epoch: 43 step: 189 loss: 0.011023472994565964
epoch: 43 step: 195 loss: 0.010211260989308357
load cnn net.
Test Accuracy of the model on the 200 eval images: 99.000000 %
Test Accuracy of the model on the 400 eval images: 99.500000 %
Test Accuracy of the model on the 600 eval images: 99.166667 %
Test Accuracy of the model on the 800 eval images: 98.875000 %
Test Accuracy of the model on the 1000 eval images: 98.600000 %
Test Accuracy of the model on the 1200 eval images: 98.500000 %
Test Accuracy of the model on the 1400 eval images: 98.571429 %
Test Accuracy of the model on the 1600 eval images: 98.562500 %
Test Accuracy of the model on the 1800 eval images: 98.555556 %
Test Accuracy of the model on the 2000 eval images: 98.600000 %
Test Accuracy of the model on the 2200 eval images: 98.590909 %
Test Accuracy of the model on the 2400 eval images: 98.458333 %
Test Accuracy of the model on the 2600 eval images: 98.269231 %
Test Accuracy of the model on the 2800 eval images: 98.285714 %
Test Accuracy of the model on the 3000 eval images: 98.300000 %
Test Accuracy of the model on the 3200 eval images: 98.343750 %
Test Accuracy of the model on the 3400 eval images: 98.352941 %
Test Accuracy of the model on the 3600 eval images: 98.333333 %
Test Accuracy of the model on the 3800 eval images: 98.342105 %
Test Accuracy of the model on the 4000 eval images: 98.350000 %
Test Accuracy of the model on the 4200 eval images: 98.309524 %
Test Accuracy of the model on the 4400 eval images: 98.386364 %
Test Accuracy of the model on the 4600 eval images: 98.434783 %
Test Accuracy of the model on the 4800 eval images: 98.354167 %
Test Accuracy of the model on the 5000 eval images: 98.320000 %
Test Accuracy of the model on the 5200 eval images: 98.326923 %
Test Accuracy of the model on the 5400 eval images: 98.296296 %
Test Accuracy of the model on the 5600 eval images: 98.250000 %
Test Accuracy of the model on the 5800 eval images: 98.293103 %
Test Accuracy of the model on the 6000 eval images: 98.300000 %
Test Accuracy of the model on the 6200 eval images: 98.306452 %
Test Accuracy of the model on the 6400 eval images: 98.296875 %
Test Accuracy of the model on the 6600 eval images: 98.303030 %
Test Accuracy of the model on the 6800 eval images: 98.264706 %
Test Accuracy of the model on the 7000 eval images: 98.242857 %
Test Accuracy of the model on the 7200 eval images: 98.208333 %
Test Accuracy of the model on the 7400 eval images: 98.229730 %
Test Accuracy of the model on the 7600 eval images: 98.250000 %
Test Accuracy of the model on the 7800 eval images: 98.230769 %
Test Accuracy of the model on the 8000 eval images: 98.187500 %
Test Accuracy of the model on the 8200 eval images: 98.182927 %
Test Accuracy of the model on the 8400 eval images: 98.178571 %
Test Accuracy of the model on the 8600 eval images: 98.174419 %
Test Accuracy of the model on the 8800 eval images: 98.204545 %
Test Accuracy of the model on the 9000 eval images: 98.200000 %
Test Accuracy of the model on the 9200 eval images: 98.184783 %
Test Accuracy of the model on the 9400 eval images: 98.180851 %
Test Accuracy of the model on the 9600 eval images: 98.208333 %
Test Accuracy of the model on the 9800 eval images: 98.204082 %
Test Accuracy of the model on the 10000 eval images: 98.190000 %
Test Accuracy of the model on the 10000 eval images: 98.190000 %
```