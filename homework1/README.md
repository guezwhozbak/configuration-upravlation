 # Shell Emulator

## Общее описание

Этот проект представляет собой эмулятор командной строки (shell) с виртуальной файловой системой. Проект написан на Python и использует библиотеку Tkinter для создания графического интерфейса. Эмулятор поддерживает основные команды командной строки, такие как `ls`, `cd`, `exit`, `rmdir`, `find`, и `mv`.

## Описание всех функций и настроек

### Функции

- **ls**: Выводит содержимое текущей директории.
- **cd**: Изменяет текущую директорию.
- **rmdir**: Удаляет пустую директорию.
- **find**: Ищет файл в указанной директории.
- **mv**: Перемещает файл или директорию.
- **exit**: Завершает работу эмулятора и сохраняет логи.

### Настройки

- **hostname**: Имя хоста, отображаемое в командной строке.
- **fs_path**: Путь к архиву с виртуальной файловой системой.
- **log_path**: Путь к файлу логов.
- **startup_script**: Путь к скрипту, который будет выполнен при запуске эмулятора.

## Описание команд для сборки проекта

Для сборки и запуска проекта выполните следующие команды:

#### Запуск тестирования
```
python -m unittest discover -s tests
```
#### Запуск эмулятора
```
python -m src.main --hostname "guezwhozbak" --fs_path "virtual_fs.zip" --log_path "log.xml" --startup_script "scripts/startup_script.sh"
```
## Примеры использования

Запуск тестирования:

![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/homework1/screenshots/hw1_2.jpg)

Запуск эмулятора:

![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/homework1/screenshots/hw1_1.jpg)

Работа эмулятора:

![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/homework1/screenshots/hw1_3.jpg)
## Результаты прогона тестов

Для запуска тестирования выполните следующую команду:
```sh
python -m unittest discover -s tests
```
Результаты тестов:
```sh
.......................................................................
----------------------------------------------------------------------
Ran 6 tests in 0.006s

OK
```
