import numpy as np
import cv2
import urllib
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
url='http://192.168.1.4:8080/shot.jpg?'
while True:
    video_stream=urllib.urlopen(url)
    imgNP=np.array(bytearray(video_stream.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNP,-1)
    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
