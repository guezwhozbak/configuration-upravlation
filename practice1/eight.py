import os
import tarfile
import argparse


def find_files_with_extension(directory, extension):
    """Находит все файлы с указанным расширением в заданной директории."""
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
