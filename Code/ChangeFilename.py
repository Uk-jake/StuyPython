import os

def changeFilename(ParentFile, FileName):
    fileDst = ParentFile + "\\" + FileName
    file_names_list = os.listdir(fileDst)

    i = 1

    for name in file_names_list:
        src = os.path.join(fileDst, name)
        dst = FileName + str(i) + '.jpg'
        dst = os.path.join(fileDst, dst)
        os.rename(src, dst)
        i += 1

file_path = 'C:\\Users\\JangUk\\Desktop\\강아지비문자료'

dirList = os.listdir(file_path)
print(dirList)

for name in dirList:
    changeFilename(file_path, name)