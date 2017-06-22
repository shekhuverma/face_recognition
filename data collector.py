import cv2,time
import sqlite3
cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#function for sqlite3 
def insert(Id,name):
    con=sqlite3.connect("database.db")
    cmd='SELECT * FROM people WHERE user_id='+str(Id)
    cursor=con.execute(cmd)
    exist=0
    for row in cursor:
        exist=1
    if exist==0:
        cmd="INSERT INTO people (user_id,name) VALUES("+"'"+str(Id)+"'"+","+"'"+str(name)+"'"+")"
        print cmd
    else:
        cmd="update people set name="+"'"+str(name)+"'"+"where user_id="+"'"+str(Id)+"'"
        print cmd
    con.execute(cmd)
    con.commit()
    con.close()
Id=raw_input('Enter your id :')
name=raw_input("Enter the name of the user :")
insert(Id,name)
sampleNum=0
for a in range(1,4,1):
    print "Data collections starts in ",a, "seconds"
    time.sleep(1)
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
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    # break if the sample number is more than
    elif sampleNum>50:
        break
cam.release()
cv2.destroyAllWindows()
