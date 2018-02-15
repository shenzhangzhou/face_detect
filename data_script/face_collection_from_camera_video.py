import cv2
def get_img(video_path,face_path):
    face_cascade = cv2.CascadeClassifier('C:\pylearning\ml&dl\\face_detect_v0\config\haarcascade_frontalface_default.xml')
    vc = cv2.VideoCapture(video_path)  # 读入视频文件
    c = 1
    if vc.isOpened():  # 判断是否正常打开
        rval, frame = vc.read()
    else:
        rval = False
    timeF = 5  # 视频帧计数间隔频率
    while rval:  # 循环读取视频帧
        rval, frame = vc.read()
        if (c % timeF == 0):
            faces = face_cascade.detectMultiScale(frame, 1.3, 5)
            # 每隔timeF帧进行存储操作
            for x, y, w, h in faces:
                f = cv2.resize(frame[y:(y + h), x:(x + w)], (128, 128))
                cv2.imwrite(face_path+'\\'+str(int(c/timeF)) + '.jpg', f)
        c+=1# 存储为图像
        cv2.waitKey(1)
    vc.release()
if __name__=="__main__":
    video=input('视频地址')
    face_path=input('保存人脸地址')
    get_img(video,face_path)
    print('ok')
