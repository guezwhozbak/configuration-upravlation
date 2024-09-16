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
