import os

path="."
isExist=os.access(path,os.F_OK)
if not isExist:
    print("File not found")
else :
    list = ["hello","Merei","Narymbek"]
    with open("file.txt","w")as file:
        for i in list:
            file.write(i+"\n")