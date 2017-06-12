import os,pickle
path=os.getcwd()
File=open("data.csv","w")
for imagepath in os.listdir(path):
    if(imagepath=="1.py" or imagepath=="data.csv"):
        continue
    else:
        File.write(imagepath)
        File.write("\n")
File.close()

