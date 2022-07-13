import os,shutil

def file_del(path):
    for file_name in os.listdir(path):
        var = path + file_name
        if os.path.isfile(var):
            print('Deleting file: ', var)
            try:
                os.remove(var)
            except PermissionError:
                print('Unable to delete file: ', var)
                pass
        elif os.path.isdir(var):
            print('Deleting dir: ', var)
            try:
                shutil.rmtree(var)
            except PermissionError:
                print('Unable to delete dir: ', var)
                pass
            
file_del("C:/Windows/Temp/")
file_del("C:/Windows/Prefetch/")
file_del("C:/Users/steve/AppData/Local/Temp/")