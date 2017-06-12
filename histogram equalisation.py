import cv2
cam = cv2.VideoCapture(0)
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    equ = cv2.equalizeHist(gray)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    cl1 = clahe.apply(gray)
    cv2.imshow("clahe",cl1)
    cv2.imshow('Normal gray',gray)
    cv2.imshow("Histogram equalised",equ)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
