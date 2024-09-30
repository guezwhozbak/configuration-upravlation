# Практическое занятие №2
Выполнила **Рожкова Ольга**, группа **ИКБО-62-23** 
---
## Задача 1
Вывести служебную информацию о пакете matplotlib (Python). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?
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
![image](https://github.com/guezwhozbak/cfg/blob/main/practice2/2-1-2.jpg)
3. Распаковываем в желаемую директорию.
---
## Задача 2
Вывести служебную информацию о пакете express (JavaScript). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?
### Установка пакета express
```
npm install express
```
### Содержимое файла со служебной информацией
![image](https://github.com/guezwhozbak/cfg/blob/main/practice2/2-2-2.jpg)
![image](https://github.com/guezwhozbak/cfg/blob/main/practice2/2-2-3.jpg)
### Основные элементы содержимого файла:
- *Name*: Название пакета.
- *Version*: Версия пакета.
- *License*: Тип лицензии.
- *Dependencies*: список зависимостей, необходимых для работы пакета.
- *Scripts*: команды, которые можно выполнять через npm.
### Как получить пакет без менеджера пакетов, прямо из репозитория?
Аналогично получению пакета matplotlib из 1-й задачи. 

[Репозиторий Express на GitHub](https://github.com/expressjs/express)
---
## Задача 3
Сформировать graphviz-код и получить изображения зависимостей express и matplotlib.
### Зависимости matplotlib и express
![image](https://github.com/guezwhozbak/cfg/blob/main/practice2/3-2.jpg)
![image](https://github.com/guezwhozbak/cfg/blob/main/practice2/3-1.jpg)
### Файл dependencies.dot (graphviz-код)
```txt
digraph dependencies {
    rankdir=LR;

    // Matplotlib dependencies
    subgraph cluster_matplotlib {
        label="Matplotlib Dependencies";
        matplotlib;
        numpy;
        pillow;
        cycler;
        kiwisolver;
        python_dateutil;
    }

    // Express dependencies
    subgraph cluster_express {
        label="Express Dependencies";
        express;
        accepts;
        array_flatten;
        body_parser;
        content_disposition;
        cookie;
        debug;
    }

    // Edges
    matplotlib -> numpy;
    matplotlib -> pillow;
    matplotlib -> cycler;
    matplotlib -> kiwisolver;
    matplotlib -> python_dateutil;

    express -> accepts;
    express -> array_flatten;
    express -> body_parser;
    express -> content_disposition;
    express -> cookie;
    express -> debug;
}
```
### Создаём изображение при помощи командной строки 
```
dot -Tpng dependencies.dot -o dependencies.png
```
### Получившееся изображение
![image](https://github.com/guezwhozbak/cfg/blob/main/practice2/dependencies.png)
### 
![image](https://github.com/guezwhozbak/cfg/blob/main/practice2/2-2-2.jpg)

