 # Учебная Виртуальная Машина (УВМ)

## Общее описание

Проект включает ассемблер и интерпретатор для учебной виртуальной машины (УВМ). Ассемблер преобразует текстовые команды в бинарный формат, а интерпретатор выполняет эти команды и сохраняет результаты в памяти.

## Описание всех функций и настроек

### Ассемблер
- **assemble(input_file, output_file, log_file)**: Преобразует текстовый файл с командами в бинарный файл и записывает логи в YAML формате.
  
- **LOAD_CONST**: Загрузка константы.
- **READ_MEM**: Чтение значения из памяти.
- **WRITE_MEM**: Запись значения в память.
- **MAX**: Бинарная операция: max()

### Интерпретатор
- **interpret(input_file, output_file, memory_range)**: Выполняет команды из бинарного файла и сохраняет значения из указанного диапазона памяти в YAML формате.

## Описание команд для сборки проекта

Ассемблер принимает на вход файл с текстом исходной программы, результатом работы ассемблера является
бинарный файл в виде последовательности байт. Дополнительный ключ командной строки задает путь к файлу-логу, в котором хранятся ассемблированные инструкции в духе списков
“ключ=значение”.
```sh
python -m assembler.assembler examples/max_program.asm examples/max_program.bin examples/max_program.yaml
```
Интерпретатор принимает на вход бинарный файл, выполняет команды УВМ
и сохраняет в файле-результате значения из диапазона памяти УВМ. Диапазон
также указывается из командной строки.
```sh
python -m interpreter.interpreter examples/max_program.bin examples/max_result.yaml 0 255
```

## Примеры использования

### Тестовая программа
Выполняем поэлементно операцию max() над двумя векторами длины 8. Результат записываем во второй вектор.

Исходный файл **max_program.asm**

![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/homework4/screenshots/hw4-1.jpg)

Запуск ассемблера:

![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/homework4/screenshots/hw4-2.png)

Файл-лог **max_program.yaml** после запуска ассемблера:

![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/homework4/screenshots/hw4-3.jpg)

Запуск интерпретатора: 

![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/homework4/screenshots/hw4-4.png)

Файл-результат **max_result.yaml**:

![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/homework4/screenshots/hw4-5.jpg)

## Результаты прогона тестов

Для запуска тестирования выполните следующую команду:

```sh
python -m unittest discover -s tests
```
Результаты тестов:
```sh
......
----------------------------------------------------------------------
Ran 6 tests in 0.037s

OK
```


