import os
#CAUTION: WILL REPLACE FILE EXTENSIONS

path =  os.getcwd()
filenames = os.listdir(path)

for filename in filenames:
        
    base = os.path.splitext(filename)[0]
    os.rename(filename, base + '.jpg')
