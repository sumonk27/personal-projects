import os

path = "D:/New folder/"
for file_name in os.listdir(path):
    var = path + file_name
    if os.path.isfile(var):
        print('Deleting file: ', var)
        os.remove(var)