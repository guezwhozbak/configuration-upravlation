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
