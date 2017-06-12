import os,cv2
import numpy as np
from PIL import Image
recognizer = cv2.face.createEigenFaceRecognizer()
path='dataset'
def getimage(path):
    IDs=[]
    faces=[]
    imagepaths=[os.path.join(path,f) for f in os.listdir(path)]
    for imagepath in imagepaths:
        ID=int(os.path.split(imagepath)[-1].split('.')[0])
        IDs.append(ID)
        faceimage=Image.open(imagepath).convert('L')
        faceNp=np.array(faceimage,'uint8')
        newfaceNp=cv2.resize(faceNp,None,300,300)
        faces.append(newfaceNp)
        cv2.imshow("Training",newfaceNp)
        cv2.waitKey(10)
    return np.array(IDs) , faces
    cv2.destroyAllwindow();
getimage(path)
IDs , faces = getimage(path)
recognizer.train(faces,IDs)
recognizer.save("data1.yml")
cv2.destroyAllWindows()

