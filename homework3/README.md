 # Config tool

## Общее описание

Этот проект представляет собой инструмент командной строки для преобразования JSON-конфигураций в учебный конфигурационный язык. Программа принимает JSON-ввод из стандартного ввода и выводит преобразованный конфигурационный язык в стандартный вывод.

## Описание всех функций и настроек

### Функции

- **parse_json(json_str)**: Парсит JSON-строку и возвращает Python-объект. В случае ошибки выводит сообщение и завершает работу.

- **convert_value(value, indent=0)**: Преобразует значение в строку в формате учебного конфигурационного языка.

- **convert_dict(d, indent=0)**: Преобразует словарь в строку в формате учебного конфигурационного языка. Проверяет, что ключи являются допустимыми идентификаторами.

- **convert_list(lst, indent=0)**: Преобразует список в строку в формате учебного конфигурационного языка.

- **evaluate_expression(expr)**: Вычисляет значение константного выражения. Поддерживает операции сложения, вычитания, а также функции `sqrt` и `ord`.

- **main()**: Основная функция, которая читает JSON-ввод из стандартного ввода, парсит его, преобразует в учебный конфигурационный язык и выводит результат.

### Настройки

- **indent**: Уровень отступа для форматирования вывода.

## Описание команд для сборки проекта

Для сборки и запуска проекта выполните следующие команды:

### Запуск тестирования: 
```sh
python -m unittest discover -s tests
```
### Запуск програмы: 
```sh
python src/main.py < input.json
```

## Примеры использования

### Работа программы

Исходные server.json, simple.json:

![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/homework3/screenshots/hw3-4.jpg)
![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/homework3/screenshots/hw3-2.jpg)

#### Результат работы программы для server.json:

![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/homework3/screenshots/hw3-5.jpg)

#### Результат работы программы для simple.json:
![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/homework3/screenshots/hw3-3.jpg)

## Результаты прогона тестов

Для запуска тестирования выполните следующую команду:
```sh
python -m unittest discover -s tests
```
Результаты тестов:
```sh
.....
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

