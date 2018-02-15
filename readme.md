#基于keras的多目标人脸识别
>目前已经可以达到在视频中自动识别人脸，并正确显示标记的地步
>本项目目的为识别特定人脸，可将所需识别的人脸照片按照不同分类放置在face文件夹下，经过训练可正确识别相应目标。同时未经训练的人脸则会显示stranger标签。
>结果如下所示：
![img_1](https://i.imgur.com/f0xxtK5.jpg)
![img_2](https://i.imgur.com/ivkD0Ev.jpg)

----------
##主要依赖库（非必须，可按自身情况进行合理替换）
  - numpy
  - keras
  - cv2
  - tensorflow
  - sklearn
  - random

----------

----------

##文件说明
  - read_data.py:读取文件夹中的图片及标签信息
  - dataSet.py:构建一个dataset类
  - train_model.py:通过构建cnn网络训练人脸模型
  - img_test.py:通过输入图片来测试模型是否正常工作
  - camera_test.py:通过输入视频来检验模型的识别率等

----------
##不足
  - 识别率较低，有时会出现识别混乱的现象
  - 图片素材数量，种类较少，可能会过拟合

----------

##改进方向
  - 尝试用其他人脸识别算法，比如ssd框架
  - 收集更多的照片进行实验
  
----------

*参考链接*

- [https://github.com/haoxinl/VideoHunter](https://github.com/haoxinl/VideoHunter "基于深度学习的视频人脸检测")
- [https://github.com/jerry1900/faceRecognition](https://github.com/jerry1900/faceRecognition "利用opencv，cnn进行人脸识别")
- [http://www.cnblogs.com/neo-T/p/6477378.html](http://www.cnblogs.com/neo-T/p/6477378.html "人脸检测及识别python实现系列")