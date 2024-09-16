# Практическое занятие №1
Выполнила **Рожкова Ольга**, группа **ИКБО-62-23** 
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
```python
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
import sys


def archive(directory, extension):
    tar_filename = f"archive_{extension.replace('.', '')}.tar"

    with tarfile.open(tar_filename, "w") as tar:
        for file in os.listdir(directory):
            if file.endswith(extension):
                tar.add(os.path.join(directory, file))
    print(f"Архив {tar_filename} создан.")


if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[2][0] != ".":
        print("Usage: ./archive.py <directory> <extension> (with .)")
    else:
        directory, extension = sys.argv[1], sys.argv[2]
        archive(directory, extension)
```
Код в консоли:
```
python3 eight.py /root/Desktop/ .py archive.tar
```
### Вывод
![image](https://github.com/guezwhozbak/cfg/blob/main/practice1/8.jpg)

## Задача 9
Написать программу, которая заменяет в файле последовательности из 4 пробелов на символ табуляции. Входной и выходной файлы задаются аргументами.
### Код
Файл 9.py
```python
import argparse

def replace_spaces_with_tab(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        content = infile.read()

    modified_content = content.replace(' ' * 4, '\t')

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(modified_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Заменить последовательности из 4 пробелов на символ табуляции.")
    parser.add_argument("input_file", help="Путь к входному файлу.")
    parser.add_argument("output_file", help="Путь к выходному файлу.")

    args = parser.parse_args()

    replace_spaces_with_tab(args.input_file, args.output_file)
    print(f"Замена завершена. Результат записан в '{args.output_file}'.")
```
Код в консоли:
```
python3 9.py input.txt output.txt
```
### Вывод
![image](https://github.com/guezwhozbak/cfg/blob/main/practice1/9.jpg)

## Задача 10
Написать программу, которая выводит названия всех пустых текстовых файлов в указанной директории. Директория передается в программу параметром.
### Код
Файл 10.py
```python
import os
import argparse


def find_empty_text_files(directory):
    empty_files = []

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path) and filename.endswith('.txt'):
            if os.path.getsize(file_path) == 0:
                empty_files.append(filename)

    return empty_files


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Найти пустые текстовые файлы в указанной директории.")
    parser.add_argument("directory", help="Путь к директории.")

    args = parser.parse_args()

    if os.path.isdir(args.directory):
        empty_files = find_empty_text_files(args.directory)
        if empty_files:
            print("Пустые текстовые файлы:")
            for file in empty_files:
                print(file)
        else:
            print("Пустых текстовых файлов не найдено.")
    else:
        print(f"Указанная директория '{args.directory}' не существует.")
```
Код в консоли:
```
python3 10.py /root/Desktop/питон
```
### Вывод
![image](https://github.com/guezwhozbak/cfg/blob/main/practice1/10.jpg)


