import cv2
import numpy as np

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0);
rec=cv2.createLBPHFaceRecognizer();
rec.load("recognizer\\trainingData.yml")
id=0
font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,2,1,0,4)
while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,200,0),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        print(conf)
        if conf>=35 and conf<=60:
            if(id==1):
                 id="puneet"
                 print("start the car")
            elif(id==2):
                 id="Shivam"
            elif(id==3):
                 id="puneet"
            elif(id==5):
                 id="Owner of car"
            else:
                 id="id not found"
            cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,100);
    cv2.imshow("Face",img);
    if(cv2.waitKey(1)==ord('q')):
        break;
cam.release()
cv2.destroyAllWindows()

