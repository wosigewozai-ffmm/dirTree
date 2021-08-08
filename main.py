import os

rootDir = 'D://JavaProject'
for dirName, subdirList, fileList in os.walk(rootDir):
    num = dirName.count("\\")
    for i in range(0,num):
        print('---', end="")
    print(dirName)
    for fname in fileList:
        for i in range(0, num):
            print('---', end="")
        print('---%s' % fname)

import zipfile

with zipfile.ZipFile('apache-maven-3.6.1.zip', 'r') as zipobj:
    for file_name in zipobj.namelist():
        info = zipobj.getinfo(file_name)
        file_name = file_name.encode('cp437').decode('gbk')
        print(file_name, info.file_size, info.compress_size)