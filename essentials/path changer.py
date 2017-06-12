import os
print os.getcwd()
for imagepaths in os.listdir(os.getcwd()):
    if imagepaths=="extension changer.py":
        continue
    else:
        for imagepath in os.listdir(imagepaths):
            temp=os.path.join(imagepaths,imagepath)
            print temp[3:]
##            final=str(imagepaths)+"_"+temp[4:]
            os.rename(temp,temp[3:])
