import os,shutil
from pyuac import main_requires_admin

@main_requires_admin 
def file_del(path):
    for file_name in os.listdir(path):
        var = path + file_name
        err = None
        if os.path.isfile(var):
            print_error(err)
            print('Deleting file: ', var)
            try:
                os.remove(var)
            except (PermissionError, RuntimeError) as err:
                pass
        elif os.path.isdir(var):
            print_error(err)
            print('Deleting dir: ', var)
            try:
                shutil.rmtree(var)
            except (RuntimeError, PermissionError) as err:
                pass

def print_error(var_type):
    if var_type is None:
        pass
    else:
        print(var_type)
       
def main():
    file_del("C:/Windows/Temp/")
    file_del("C:/Windows/Prefetch/")
    file_del("C:/Users/steve/AppData/Local/Temp/")

if __name__ == "__main__":
    main()