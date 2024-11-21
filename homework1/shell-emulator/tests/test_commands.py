"Тесты для команд"

import unittest
import os
import shutil
from src.commands import cd, mv, rmdir, find, ls

class TestCommands(unittest.TestCase):

    def setUp(self): # Метод setUp выполняется перед каждым тестом для настройки тестовой среды
        # Создаем временную директорию для тестирования
        self.test_dir = 'test_dir'
        os.makedirs(self.test_dir, exist_ok=True)
        # Сохраняем текущий рабочий каталог
        self.original_cwd = os.getcwd()

    def tearDown(self): # Метод tearDown выполняется после каждого теста для очистки тестовой среды
        # Удаляем временную директорию после тестирования
        shutil.rmtree(self.test_dir)
        os.chdir(self.original_cwd)

    def test_cd(self):
        # Изменяем текущий рабочий каталог на временную директорию
        os.chdir(self.test_dir)
        # Вызываем команду cd для перехода на уровень выше и возврата в исходный рабочий каталог
        cd('..', self.original_cwd)
        # Проверяем, что текущий рабочий каталог совпадает с исходным рабочим каталогом
        self.assertEqual(os.getcwd(), self.original_cwd)

    def test_mv(self):
        # Создаем путь к исходному и целевому файлу
        src = os.path.join(self.test_dir, 'src_file')
        dst = os.path.join(self.test_dir, 'dst_file')
        with open(src, 'w') as f:
            f.write('test')
        mv(src, dst)
        # Проверяем, что исходный файл больше не существует, а целевой существует
        self.assertFalse(os.path.exists(src))
        self.assertTrue(os.path.exists(dst))

    def test_rmdir(self):
        # Создаем путь к поддиректории и ее саму
        sub_dir = os.path.join(self.test_dir, 'sub_dir')
        os.makedirs(sub_dir, exist_ok=True)
        rmdir(sub_dir)
        # Проверяем, что поддиректория больше не существует
        self.assertFalse(os.path.exists(sub_dir))

    def test_find(self):
        # Создаем путь к тестовому файлу
        test_file = os.path.join(self.test_dir, 'test_file')
        with open(test_file, 'w') as f:
            f.write('test')
        result = find(self.test_dir, 'test_file')
        # Проверяем, что результат поиска совпадает с путем к тестовому файл
        self.assertEqual(result, test_file)

    def test_ls(self):
        # Создаем путь к тестовому файлу
        test_file = os.path.join(self.test_dir, 'test_file')
        with open(test_file, 'w') as f:
            f.write('test')
        result = ls(self.test_dir)
        # Проверяем, что 'test_file' присутствует в результате команды ls
        self.assertIn('test_file', result)

if __name__ == '__main__':
    unittest.main()




