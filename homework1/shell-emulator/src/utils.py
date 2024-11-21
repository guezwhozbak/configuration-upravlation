import zipfile

def extract_fs(zip_path, extract_path):
    # Открываем архив в заданном пути в режиме чтения
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        #Экспортируем всё в указанную директорию
        zip_ref.extractall(extract_path)
