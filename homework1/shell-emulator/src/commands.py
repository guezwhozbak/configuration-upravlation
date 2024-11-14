"Реализация команд"

import os
import shutil

def cd(path, root_path):
    new_path = os.path.abspath(os.path.join(os.getcwd(), path))
    if new_path.startswith(root_path):
        os.chdir(new_path)
    else:
        raise ValueError("You are in the root directory of the file system")

def mv(src, dst):
    shutil.move(src, dst)

def rmdir(path):
    os.rmdir(path)

def find(path, name):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
    return None

def ls(path):
    return os.listdir(path)





