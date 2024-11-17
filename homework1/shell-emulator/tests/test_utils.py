"Тесты для вспомогательных функций"

import unittest
import os
import shutil
import zipfile
from src.utils import extract_fs

# Определяем класс TestUtils, который наследуется от unittest.TestCase
class TestUtils(unittest.TestCase):
    def setUp(self):
        # Создаем временную директорию для тестирования
        self.test_dir = 'test_dir'
        os.makedirs(self.test_dir, exist_ok=True)
        self.zip_path = os.path.join(self.test_dir, 'test.zip')
        self.extract_path = os.path.join(self.test_dir, 'extracted')

    def tearDown(self):
        # Удаляем временную директорию после тестирования
        shutil.rmtree(self.test_dir)

    def test_extract_fs(self):
        # Создаем временный файл для добавления в ZIP-архив
        test_file_path = os.path.join(self.test_dir, 'test_file.txt')
        with open(test_file_path, 'w') as f:
            f.write('test content')

        # Создаем ZIP-архив и добавляем в него временный файл
        with zipfile.ZipFile(self.zip_path, 'w') as zip_ref:
            zip_ref.write(test_file_path, arcname='test_file.txt')

        # Извлекаем содержимое ZIP-архива
        extract_fs(self.zip_path, self.extract_path)

        # Проверяем, что файл был извлечен правильно
        extracted_file_path = os.path.join(self.extract_path, 'test_file.txt')
        self.assertTrue(os.path.exists(extracted_file_path))
        with open(extracted_file_path, 'r') as f:
            content = f.read()
        self.assertEqual(content, 'test content')

if __name__ == '__main__':
    unittest.main()
