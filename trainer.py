import os,cv2
import numpy as np
from PIL import Image
recognizer = cv2.face.createLBPHFaceRecognizer()
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
        faces.append(faceNp)
        cv2.imshow("Training",faceNp)
        cv2.waitKey(10)
    return np.array(IDs) , faces
    cv2.destroyAllwindow();
getimage(path)
IDs , faces = getimage(path)
recognizer.train(faces,IDs)
recognizer.save("data.yml")
cv2.destroyAllWindows()

