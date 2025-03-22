import os

def list_contests(path):
    all_items = os.listdir(path)
    
    directories = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
    files = [item for item in all_items if os.path.isfile(os.path.join(path, item))]
    
    print("List of directories:")
    for directory in directories:
        print(directory)
        
    print("\nList of files:")
    for file in files:
        print(file)
        
    print("\nFull list of contents")
    for item in all_items:
        print(item)
        
specified_path = r"C:\Users\user\Desktop\python\lab6"
list_contests(specified_path)