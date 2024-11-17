import zipfile
import xml.etree.ElementTree as ET
import os
import logging
import tkinter as tk
from tkinter import simpledialog
from src.commands import ls, cd, rmdir, find, mv

# Настройка логирования
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class ShellGUI:
    def __init__(self, hostname, fs_path, log_path, startup_script):
        self.hostname = hostname
        self.fs_path = fs_path
        self.log_path = log_path
        self.startup_script = startup_script
        self.fs = self.load_fs()
        self.log = []
        self.root_path = os.path.abspath('virtual_fs')

        # Сохраняем исходный рабочий каталог (для последующего сохранения там лог-файла)
        self.original_cwd = os.getcwd()

        # Создаем основное окно приложения
        self.root = tk.Tk()
        self.root.title(f"{self.hostname} Shell Emulator")

        # Создаем текстовое поле для вывода результатов команд
        self.output_text = tk.Text(self.root, height=20, width=80)
        self.output_text.pack()

        # Создаем поле ввода для команд
        self.input_entry = tk.Entry(self.root, width=80)
        self.input_entry.pack()
        # Привязываем событие нажатия Enter к методу execute_command
        self.input_entry.bind('<Return>', self.execute_command)

    def load_fs(self):
        # Проверяем, существует ли файл по указанному пути
        logging.debug(f"Loading virtual file system from {self.fs_path}")
        if not os.path.exists(self.fs_path):
            logging.error(f"File {self.fs_path} does not exist")
            raise FileNotFoundError(f"File {self.fs_path} does not exist")

        try:
            # Открываем ZIP-архив в режиме чтения, извлекаем всё
            with zipfile.ZipFile(self.fs_path, 'r') as zip_ref:
                zip_ref.extractall('virtual_fs')
                logging.debug(f"Extracted virtual file system to 'virtual_fs'")
        except zipfile.BadZipFile as e:
            logging.error(f"Error loading virtual file system: {e}")
            raise

        # Устанавливаем текущий рабочий каталог на корневую директорию виртуальной файловой системы
        os.chdir('virtual_fs')
        return 'virtual_fs'

    def run(self):
        self.execute_startup_script()
        self.root.mainloop()

    def execute_startup_script(self):
        # Проверяем, существует ли файл стартового скрипта
        logging.debug(f"Executing startup script from {self.startup_script}")
        if not os.path.exists(self.startup_script):
            logging.error(f"File {self.startup_script} does not exist")
            raise FileNotFoundError(f"File {self.startup_script} does not exist")

        # Открываем файл, читаем построчно, добавляем команды из стартового скрипта в лог, выполняем
        with open(self.startup_script, 'r') as file:
            for line in file:
                self.log.append(line.strip())
                self.execute_command_from_script(line.strip())

    def execute_command_from_script(self, command):
        # self.log.append(command)
        self.execute_command(command)

    def execute_command(self, event=None):
        # Получаем введённый текст, добавляем в лог, очищаем поле ввода
        command = self.input_entry.get()
        self.log.append(command)
        self.input_entry.delete(0, tk.END)

        # Разбиваем команду на части, если пустая завершаем выполнение
        parts = command.split()
        if not parts:
            return

        cmd = parts[0] # Извлекаем имя команды
        args = parts[1:] #Аргументы

        self.output_text.insert(tk.END, f"{self.hostname} $ {command}\n")

        if cmd == 'ls':
            if cmd.strip() != 'ls':
                self.output_text.insert(tk.END, f"Error: Command '{cmd}' contains trailing spaces and is not valid\n")
                return
            if args:
                path = args[0] # Если у команды есть аргументы, используем первый аргумент как путь
            else:
                path = os.getcwd() # Иначе используем текущий рабочий каталог
            result = ls(path)
            for item in result:
                self.output_text.insert(tk.END, item + '\n')
        elif cmd == 'cd':
            if args:
                path = args[0]
                try:
                    cd(path, self.root_path)
                except ValueError as e:
                    self.output_text.insert(tk.END, f"{e}\n")
        elif cmd == 'exit':
            self.save_log()
            self.root.quit()
        elif cmd == 'rmdir':
            if args:
                path = args[0]
                rmdir(path)
        elif cmd == 'find':
            if len(args) >= 2:
                path = args[0]
                name = args[1]
                result = find(path, name)
                if result:
                    self.output_text.insert(tk.END, result + '\n')
                else:
                    self.output_text.insert(tk.END, f"{name} not found in {path}\n")
        elif cmd == 'mv':
            if len(args) >= 2:
                src = args[0]
                dst = args[1]
                mv(src, dst)
        else:
            self.output_text.insert(tk.END, f"Unknown command: {cmd}\n")

    def save_log(self):
        logging.debug(f"Saving log to {self.log_path}")

        # Временно изменяем текущий рабочий каталог на исходный
        os.chdir(self.original_cwd)

        # Очищаем файл лога перед записью новых записей
        with open(self.log_path, 'w') as f:
            f.write('')

        root = ET.Element('log')# Создаем корневой элемент в XML

        # Добавляем каждую команду из лога в XML-документ
        for cmd in self.log:
            ET.SubElement(root, 'command').text = cmd
        tree = ET.ElementTree(root)# Создаем объект ElementTree с корневым элементом
        tree.write(self.log_path)
        logging.debug(f"Log saved to {self.log_path}")

        os.chdir(self.root_path)





















