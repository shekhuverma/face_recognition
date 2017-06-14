import cv2
cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
Id=raw_input('enter your id')
sampleNum=0
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
##        preprocessing 
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(5,5))
    cl1 = clahe.apply(gray)
    gray=cv2.medianBlur(cl1,3)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        #incrementing sample number
        sampleNum=sampleNum+1
        #saving the captured face in the dataset folder
        cv2.imwrite("dataSet/"+str(Id) +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('frame',img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    # break if the sample number is morethan 20
    elif sampleNum>150:
        break
cam.release()
cv2.destroyAllWindows()
