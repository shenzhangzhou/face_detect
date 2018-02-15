import cv2
from PIL import Image
import matplotlib.pyplot as plt
import os
from os import listdir
from os.path import isfile, join
img_floder='face\person0_img'
face_floder='face\person0_face\\'
flag=1
# 因为是手机拍摄所以需要旋转视频
def get_img(video_path='video.mp4'):
    vc = cv2.VideoCapture(video_path)  # 读入视频文件
    c = 1
    if vc.isOpened():  # 判断是否正常打开
        rval, frame = vc.read()
    else:
        rval = False
    timeF = 10  # 视频帧计数间隔频率
    while rval:  # 循环读取视频帧
        rval, frame = vc.read()
        if (c % timeF == 0):# 每隔timeF帧进行存储操作
            cv2.imwrite(img_floder+'\\'+str(int(c/timeF)) + '.jpg', frame)  # 存储为图像
        c = c + 1
        cv2.waitKey(1)
    vc.release()
def img_rotate(folder):
    Path=listdir(folder)
    c=0
    for path in Path:
        c+=1
        new_path=join(folder,path)
        img = Image.open(new_path)
        new_img = img.rotate(270)
        new_img.save('face\person0_img\\'+str(c)+'.jpg')

def get_face(Path,objectPath,num):
    face_cascade = cv2.CascadeClassifier('config/haarcascade_frontalface_default.xml')
    im = cv2.imread(Path)
    faces = face_cascade.detectMultiScale(im, 1.3, 5)
    for x, y, w, h in faces:
        f = cv2.resize(im[y:(y + h), x:(x + w)], (100, 100))
        cv2.imwrite(objectPath + str(num) +'.jpg', f)
def get_path(path):
    try:
        s = os.listdir(path)
        resultArray = []
        for i in s:
            document = os.path.join(path, i)
            resultArray.append(document)
    except IOError:
        print ("Error")
    else:
        print ("读取成功")
        return resultArray
if __name__=="__main__":
    get_img()
    if flag==1:
        img_rotate(img_floder)
    else:
        pass
    img_path = get_path(img_floder)
    for path in img_path:
        get_face(path,face_floder,img_path.index(path))
    print('ok')


