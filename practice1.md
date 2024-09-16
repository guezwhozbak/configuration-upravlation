# Практическое занятие №1
## Задача 1
Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd.
### Код
```
grep '^[^:]*' /etc/passwd | cut -d: -f1 | sort
```
### Вывод
![image](https://github.com/guezwhozbak/cfg/blob/main/practice1/1.jpg)

## Задача 2
Вывести данные /etc/protocols в отформатированном и отсортированном порядке для 5 наибольших портов.
### Код
```
cat /etc/protocols | awk '{print $2, $1}' | sort -nr | head -n 5
```
### Вывод
![image](https://github.com/guezwhozbak/cfg/blob/main/practice1/2.jpg)

## Задача 3
Написать программу banner средствами bash для вывода текстов.
### Код на Python
```
x = input()
print('+', end="")
y = [print('-', end="") for i in range(len(x) + 2)]
print('+')
print(f"| {x} |")
print('+', end="")
y = [print('-', end='') for i in range(len(x) + 2)]
print("+")
```
### Вывод
![image](https://github.com/guezwhozbak/cfg/blob/main/practice1/3.jpg)

## Задача 4
Написать программу для вывода всех идентификаторов (по правилам C/C++ или Java) в файле (без повторений).
### Код
```
grep -E -o '\b[a-zA-Z_][a-zA-Z0-9_]*\b' hello.c | uniq
```
### Вывод
![image](https://github.com/guezwhozbak/cfg/blob/main/practice1/4.jpg)

## Задача 5
Написать программу для регистрации пользовательской команды (правильные права доступа и копирование в /usr/local/bin).
### Код
Файл 5.sh :
```
#!/bin/bash
echo "Hello, world!"
```
```
chmod +x 5.sh
sudo mv 5.sh /usr/local/bin/5
```
### Вывод
![image](https://github.com/guezwhozbak/cfg/blob/main/practice1/5.jpg)

## Задача 6
Написать программу для проверки наличия комментария в первой строке файлов с расширением c, js и py.
### Код
Файл main.py:
```python
# -*- coding: utf-8 -*-
import os
import sys

def check_comment_in_first_line(file_path):
    with open(file_path, 'r') as file:
        first_line = file.readline().strip()
        if first_line.startswith('#') or first_line.startswith('//') or first_line.startswith('/*'):
            return True
    return False

def check_files_in_directory(directory):
    extensions = ('.c', '.js', '.py')
    for filename in os.listdir(directory):
        if filename.endswith(extensions):
            file_path = os.path.join(directory, filename)
            if check_comment_in_first_line(file_path):
                print(f"Комментарий найден в файле: {filename}")
            else:
                print(f"Комментарий не найден в файле: {filename}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Использование: python3 main.py ~/Desktop/питон")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"{directory} не является директорией.")
        sys.exit(1)

    check_files_in_directory(directory)
```
Код в консоли:
```
python3 main.py ~/Desktop/питон
```
### Вывод
![image](https://github.com/guezwhozbak/cfg/blob/main/practice1/6.jpg)

## Задача 7
Написать программу для нахождения файлов-дубликатов (имеющих 1 или более копий содержимого) по заданному пути (и подкаталогам).
### Код
Файл 7.py
```python
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
```
Код в консоли:
```
python3 7.py
```
### Вывод
![image](https://github.com/guezwhozbak/cfg/blob/main/practice1/7.jpg)

## Задача 8
Написать программу, которая находит все файлы в данном каталоге с расширением, указанным в качестве аргумента и архивирует все эти файлы в архив tar.
### Код
Файл eight.py
```python
import os
import tarfile
import argparse


def find_files_with_extension(directory, extension):
    matched_files = []
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(extension):
                matched_files.append(os.path.join(dirpath, filename))
    return matched_files


def create_tar_archive(files, output_filename):
    with tarfile.open(output_filename, 'w') as tar:
        for file in files:
            tar.add(file, arcname=os.path.basename(file))
    print(f"Архив '{output_filename}' успешно создан.")


if __name__ == "__eight__":
    parser = argparse.ArgumentParser(description="Найти файлы с указанным расширением и архивировать их.")
    parser.add_argument("directory", help="Путь к директории для поиска файлов.")
    parser.add_argument("extension", help="Расширение файлов для поиска (например, .txt).")
    parser.add_argument("output", help="Имя выходного файла архива (например, archive.tar).")

    args = parser.parse_args()

    files_to_archive = find_files_with_extension(args.directory, args.extension)

    if files_to_archive:
        create_tar_archive(files_to_archive, args.output)
    else:
        print(f"Файлы с расширением '{args.extension}' не найдены в директории '{args.directory}'.")
```
Код в консоли:
```
python3 eight.py /root/Desktop/ .py archive.tar
```
### Вывод
Отсутствует

## Задача 9
Написать программу, которая заменяет в файле последовательности из 4 пробелов на символ табуляции. Входной и выходной файлы задаются аргументами.
### Код
```
grep '^[^:]*' /etc/passwd | cut -d: -f1 | sort
```
### Вывод
![image](https://github.com/guezwhozbak/cfg/blob/main/practice1/1.jpg)

## Задача 10
Написать программу, которая выводит названия всех пустых текстовых файлов в указанной директории. Директория передается в программу параметром.
### Код
```
grep '^[^:]*' /etc/passwd | cut -d: -f1 | sort
```
### Вывод
![image](https://github.com/guezwhozbak/cfg/blob/main/practice1/1.jpg)


