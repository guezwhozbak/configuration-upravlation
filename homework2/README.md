# Git Commit Dependency Visualizer

## Общее описание

Этот инструмент командной строки визуализирует граф зависимостей коммитов в git-репозитории, включая транзитивные зависимости.

## Описание всех функций и настроек

- `--graphviz_path`: Путь к программе для визуализации графов (Graphviz).
- `--repo_path`: Путь к анализируемому репозиторию.
- `--date`: Дата коммитов в репозитории (формат YYYY-MM-DD).

## Описание команд для сборки проекта

python -m unittest discover -s tests
```bash
pip install -r requirements.txt
python src/main.py --graphviz_path /path/to/graphviz --repo_path /path/to/repo --date YYYY-MM-DD
```

## Примеры использования

![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/homework2/screenshots/hw2_1.jpg)
![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/homework2/screenshots/hw2_2.jpg)

## Результаты прогона тестов

#### Команда для запуска тестов
```
python -m unittest discover -s src/tests
```
#### Результаты тестов
```
.
----------------------------------------------------------------------
Ran 1 test in 0.121s

OK
```
