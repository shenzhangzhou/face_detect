import cv2
import os

def get_face(Path,objectPath,num):
    face_cascade = cv2.CascadeClassifier('C:\pylearning\ml&dl\\face_detect_v0\config\haarcascade_frontalface_default.xml')
    im = cv2.imread(Path)
    faces = face_cascade.detectMultiScale(im, 1.3, 5)
    for x, y, w, h in faces:
        f = cv2.resize(im[y:(y + h), x:(x + w)], (128, 128))
        cv2.imwrite(objectPath+'\\' + str(num) +'.jpg', f)
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
    img_floder=input('图片文件夹的地址')
    img_path=get_path(img_floder)
    face_path=input('目的文件夹的地址')
    for path in img_path:
        get_face(path,face_path,img_path.index(path))
    print('ok')
