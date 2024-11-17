"Тесты для команд"

import unittest
import os
import shutil
from src.commands import cd, mv, rmdir, find, ls

class TestCommands(unittest.TestCase):

    def setUp(self):
        # Создаем временную директорию для тестирования
        self.test_dir = 'test_dir'
        os.makedirs(self.test_dir, exist_ok=True)
        self.original_cwd = os.getcwd()

    def tearDown(self):
        # Удаляем временную директорию после тестирования
        shutil.rmtree(self.test_dir)
        os.chdir(self.original_cwd)

    def test_cd(self):
        # Тестирование команды cd
        os.chdir(self.test_dir)
        cd('..', self.original_cwd)
        self.assertEqual(os.getcwd(), self.original_cwd)

    def test_mv(self):
        # Тестирование команды mv
        src = os.path.join(self.test_dir, 'src_file')
        dst = os.path.join(self.test_dir, 'dst_file')
        with open(src, 'w') as f:
            f.write('test')
        mv(src, dst)
        self.assertFalse(os.path.exists(src))
        self.assertTrue(os.path.exists(dst))

    def test_rmdir(self):
        # Тестирование команды rmdir
        sub_dir = os.path.join(self.test_dir, 'sub_dir')
        os.makedirs(sub_dir, exist_ok=True)
        rmdir(sub_dir)
        self.assertFalse(os.path.exists(sub_dir))

    def test_find(self):
        # Тестирование команды find
        test_file = os.path.join(self.test_dir, 'test_file')
        with open(test_file, 'w') as f:
            f.write('test')
        result = find(self.test_dir, 'test_file')
        self.assertEqual(result, test_file)

    def test_ls(self):
        # Тестирование команды ls
        test_file = os.path.join(self.test_dir, 'test_file')
        with open(test_file, 'w') as f:
            f.write('test')
        result = ls(self.test_dir)
        self.assertIn('test_file', result)

if __name__ == '__main__':
    unittest.main()
