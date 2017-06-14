import cv2,time,matplotlib
import numpy as np
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load("data.yml")
cam=cv2.VideoCapture(0)
Id=0
last_time=time.time()
print last_time
while True:
    ret,img=cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 1)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
        Id,config=recognizer.predict(gray[y:y+h,x:x+w])
        if config<75:
            if Id==1:
                name="shekhar"
        else:
            name="else"
        cv2.putText(img,str(name), (x+5,y+h),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
    cv2.imshow("MY TRY",img)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    print "Frame rate == " ,1/(time.time()-last_time)
    last_time=time.time()
cam.release()
cv2.destroyAllWindows()
