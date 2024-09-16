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