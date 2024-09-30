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
![image](https://github.com/guezwhozbak/cfg/blob/main/practice1/1.jpg)
