import os
import hashlib
from collections import defaultdict

def find_duplicates(directory):
    hash_dict = defaultdict(list)

    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_hash = hash_file(file_path)
            hash_dict[file_hash].append(file_path)

    duplicates = {hash_value: paths for hash_value, paths in hash_dict.items() if len(paths) > 1}

    return duplicates

def hash_file(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

if __name__ == "__main__":
    directory_to_search = input("Введите путь к директории: ")
    duplicates = find_duplicates(directory_to_search)

    if duplicates:
        print("Найдены дубликаты:")
        for hash_value, paths in duplicates.items():
            print(f"\nХеш: {hash_value}")
            for path in paths:
                print(f"  {path}")
    else:
        print("Дубликаты не найдены.")