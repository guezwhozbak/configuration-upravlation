# Практическое занятие №4 "Системы контроля версий"
Выполнила **Рожкова Ольга**, группа **ИКБО-62-23** 
---
## Задача №1

На сайте с помощью команд эмулятора git получить аналогичное картинке из задания состояние проекта (сливаем master с first, перебазируем second на master).

### Решение

#### Получившееся состояние

![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/practice4/4-1.jpg)

#### Использованные команды git

![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/practice4/4-2.jpg)

#### Перебазирование second на master

![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/practice4/4-3.jpg)

#### Слияние master с first

![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/practice4/4-4.jpg)

## Задача №2

Создать локальный git-репозиторий. Задать свои имя и почту (далее – coder1). Разместить файл prog.py с какими-нибудь данными. Прислать в текстовом виде диалог с git.

### Решение

#### Диалог с Git:

```
$ mkdir mirea
$ cd mirea
$ git init
Initialized empty Git repository in C:/Users/guezwhozbak/mirea/.git/
$ git config user.name "guezwhozbak"
$ git config user.email "rozhkova_olya@list.ru"
$ echo "print ('выпал снег')" > prog.py
$ git add prog.py
$ git commit -m "Initial commit with prog.py"
[master (root-commit) b484d1f] Initial commit with prog.py
 1 file changed, 1 insertion(+)
 create mode 100644 prog.py
```


## Задача №3

Создать рядом с локальным репозиторием bare-репозиторий с именем server. Загрузить туда содержимое локального репозитория. Команда git remote -v должна выдать информацию о server! Синхронизировать coder1 с server.

Клонировать репозиторий server в отдельной папке. Задать для работы с ним произвольные данные пользователя и почты (далее – coder2). Добавить файл readme.md с описанием программы. Обновить сервер.

Coder1 получает актуальные данные с сервера. Добавляет в readme в раздел об авторах свою информацию и обновляет сервер.

Coder2 добавляет в readme в раздел об авторах свою информацию и решает вопрос с конфликтами.

Прислать список набранных команд и содержимое git log.

### Решение

#### Список набранных команд 

```
# Создание bare-репозитория server
git init --bare server

# Загрузка содержимого локального репозитория в server
cd mirea
git remote add origin ../server
git push -u origin master

# Проверка информации о remote
git remote -v

# Синхронизация coder1 с server
git pull origin master

# Клонирование репозитория server в отдельную папку для coder2
git clone ../server coder2_repo
cd coder2_repo

# Задание имени и почты для coder2
git config user.name "Vasya Pupkin"
git config user.email "Vase4ka1337@mail.ru"

# Добавление файла readme.md с описанием программы
echo "# Program\n\nThis is a description of the program" > readme.md
git add readme.md
git commit -m "Add readme.md"
git push origin master

# Обновление coder1 с сервера
cd ~/mirea
git pull origin master

# Добавление информации о coder1 в readme.md
echo "\n## Authors\n\n- coder1" >> readme.md
git add readme.md
git commit -m "Add guezwhozbak info"
git push origin master

# Обновление coder2 с сервера и добавление информации о coder2 в readme.md
cd ../coder2_repo
git pull origin master
echo "\n- Vasya Pupkin >> readme.md
git add readme.md
git commit -m "Add Vasya Pupkin info"
git push origin master

# Решение конфликтов
git pull origin master
# Решение конфликтов вручную
git add readme.md
git commit -m "Resolve merge conflict"
git push origin master
```

#### Содержимое git log
```
commit 2e186c3ae2bcab57e4d4415b867f1db8a4603004 (HEAD -> master, origin/master, origin/HEAD)
Merge: aff69b2 3beaad3
Author: Vasya Pupkin <Vase4ka1337@mail.ru>
Date: Wed Nov 6 20:27:28 2024 +0300

Resolve merge conflict

commit aff69b26a104c3e8609c9822a9c20ccd9b083cfe
Author: Vasya Pupkin <Vase4ka1337@mail.ru>
Date: Wed Nov 6 20:26:30 2024 +0300

Add Vasya Pupkin info

commit 3beaad3450b6c4cdd57fb2b64eeaad9cdecda007
Author: guezwhozbak <rozhkova_olya@list.ru>
Date: Wed Nov 6 20:23:47 2024 +0300

Add guezwhozbak info

commit b484d1f8b08f72e5d905fcadbf086df6ad9aed93
Author: guezwhozbak <rozhkova_olya@list.ru>
Date: Wed Nov 6 20:12:01 2024 +0300

Initial commit with prog.py
```

## Задача №4

Написать программу на Питоне (или другом ЯП), которая выводит список содержимого всех объектов репозитория. Воспользоваться командой "git cat-file -p". Идеальное решение – не использовать иных сторонних команд и библиотек для работы с git.

## Решение

#### objects_git.py

```python
import subprocess

def get_git_objects():
    # получаем список всех объектов в репозитории
    result = subprocess.run(['git', 'rev-list', '--all'], capture_output=True, text=True)
    if result.returncode != 0:
        print("Ошибка при получении списка объектов:", result.stderr)
        return []
    return result.stdout.splitlines()

def get_object_content(object_id):
    # получаем содержимое объекта
    result = subprocess.run(['git', 'cat-file', '-p', object_id], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Ошибка при получении содержимого объекта {object_id}:", result.stderr)
        return None
    return result.stdout

def main():
    objects = get_git_objects()
    if not objects:
        print("Нет объектов в репозитории.")
        return

    for object_id in objects:
        content = get_object_content(object_id)
        if content:
            print(f"Object ID: {object_id}")
            print(content)
            print("-" * 40)

if __name__ == "__main__":
    main()
```

#### Использование команды "git cat-file -p"
```
$ git cat-file -p 3beaad3450b6c4cdd57fb2b64eeaad9cdecda007
tree 7be9fbad04fbde7e016192bfaf48fff15c07f13d
parent b484d1f8b08f72e5d905fcadbf086df6ad9aed93
author guezwhozbak <rozhkova_olya@list.ru> 1730913827 +0300
committer guezwhozbak <rozhkova_olya@list.ru> 1730913827 +0300

Add guezwhozbak info
```
