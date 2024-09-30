# Практическое занятие №2
Выполнила **Рожкова Ольга**, группа **ИКБО-62-23** 
## Задача 1
Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd.
### Код на Python
```python
import importlib.metadata

def print_package_metadata(package_name):
    try:
        pkg_metadata = importlib.metadata.metadata(package_name)

        print(f"Служебная информация о пакете '{package_name}':\n")
        for key, value in pkg_metadata.items():
            print(f"{key}: {value}")

    except importlib.metadata.PackageNotFoundError:
        print(f"Пакет '{package_name}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

print_package_metadata('matplotlib')
```
### Вывод
![image](https://github.com/guezwhozbak/cfg/blob/main/practice2/2-1.jpg)

### Основные элементы содержимого файла:

- *Name*: Название пакета.

- *Version*: Версия пакета.

- *Summary*: Краткое описание.

- *Homepage*: URL-адрес домашней страницы проекта.

- *Author*: Имя автора или команды авторов.

- *Author-email*: Электронная почта автора.

- *License*: Лицензия, под которой распространяется пакет.

- *Requires-Dist*: Список зависимостей, необходимых для работы пакета.

- *Description*: Более подробное описание пакета. (не видно на скриншоте)
### Как получить пакет без менеджера пакетов, прямо из репозитория?
1. Переходим на страничку репозитория, например, [matplotlib на GitHub](https://github.com/matplotlib/matplotlib).
![image](https://github.com/guezwhozbak/cfg/blob/main/practice2/2-1-1.jpg)
2. Нажимаем на "Code" и выбираем "Download ZIP", чтобы скачать архив с исходным кодом.
![image](https://github.com/guezwhozbak/cfg/blob/main/practice2/2-1-1.jpg)
3. Распаковываем в желаемую директорию.
   
