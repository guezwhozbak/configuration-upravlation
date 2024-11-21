"Реализация команд"

import os
import shutil

def cd(path, root_path):
    # Создаем абсолютный путь на основе текущего рабочего каталога и переданного пути
    new_path = os.path.abspath(os.path.join(os.getcwd(), path))
    # Проверяем, что новый путь находится внутри корневой директории вфс
    if new_path.startswith(root_path):
        # Изменяем текущий рабочий каталог на новый путь
        os.chdir(new_path)
    else:
        # Выбрасываем исключение, если попытка выйти за пределы корневой директории1
        raise ValueError("You are in the root directory of the file system")

def mv(src, dst):
    # Перемещаем из инзачальной директории в целевую с помощью модуля shutil
    shutil.move(src, dst)

def rmdir(path):
    # Удаляем директорию по указ. пути с помощью модуля os
    os.rmdir(path)

def find(path, name):
    # os.walk для обхода всех директорий и файлов в указанном пути
    for root, dirs, files in os.walk(path):
        # Проверяем, содержится ли имя файла в списке файлов текущей дир.
        if name in files:
            return os.path.join(root, name)
    return None

def ls(path):
    # Получаем список всех файлов и директорй в указ. пути
    return os.listdir(path)





