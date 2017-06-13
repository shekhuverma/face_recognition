import cv2
import numpy as np
cam = cv2.VideoCapture(0)
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faceNp=np.asarray(gray)
    equ = cv2.equalizeHist(gray)
    clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(5,5))
    cl1 = clahe.apply(gray)
    norm_image = cv2.normalize(faceNp, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    cv2.imshow("Normalized",norm_image)
    cv2.imshow("clahe",cl1)
    cv2.imshow('Normal gray',gray)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
