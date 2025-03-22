import os 

def check_access(path):
    if os.access(path, os.F_OK):
        print("Path exists.")
    else:
        print("Path does not exist.")
        return

    if os.access(path, os.R_OK):
        print("Readable.")
    else:
        print("Not readable.")
        
    if os.access(path, os.W_OK):
        print("Writable.")
    else:
        print("Not writable.")
        
    if os.access(path, os.X_OK):
        print("Executable.")
    else:
        print("Not executable.")
        
specified_path = r"C:\Users\user\Desktop\python\lab6"
check_access(specified_path)