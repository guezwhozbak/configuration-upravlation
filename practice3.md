# Практическое занятие №3
Выполнила **Рожкова Ольга**, группа **ИКБО-62-23** 
---
## Задача №1
Реализовать на Jsonnet приведенный ниже пример в формате JSON. Использовать в реализации свойство программируемости и принцип DRY.

## Решение

Свойством программируемости можно назвать способность системы легко модифицироваться и расширяться, т. е. разработчик может легко добавить новые функции и легко изменить уже существующие.

Принцип DRY (Don't Repeat Yourself) говорит о том, что "не следует повторять себя". Это значит, что информация или логика должны быть определены в одном месте, чтобы избежать дублирования. Это помогает уменьшить количество ошибок и сделать код более читабельным. Если вдруг надо будет внести изменения, то потребуется сделать их только в одном месте.

### Реализация на Jsonnet
```Jsonnet
// groups.jsonnet
local groupPrefix = "ИКБО-";
local groupYear = "-20";

local groups = [groupPrefix + std.str(i) + groupYear for i in std.range(1, 63)];

local students = [
  { age: 19, group: "ИКБО-4-20", name: "Иванов И. И." },
  { age: 18, group: "ИКБО-5-20", name: "Петров П.П." },
  { age: 18, group: "ИКБО-5-20", name: "Сидоров С.С." },
  { age: 33, group: "ИКБО-62-23", name: "Тревис Скотт" }
];

{
  groups: groups,
  students: students,
  subject: "Конфигурационное управление",
}

```


## Задача №2
Реализовать на Dhall приведенный ниже пример в формате JSON. Использовать в реализации свойство программируемости и принцип DRY.

### Реализация на Dhall
```Dhall
let Group = Text
let Student = { age : Natural, group : Group, name : Text }

let groups = List (Group) [ "ИКБО-1-20", "ИКБО-2-20", "ИКБО-3-20", "ИКБО-4-20", "ИКБО-5-20", "ИКБО-6-20", 
                             "ИКБО-7-20", "ИКБО-8-20", "ИКБО-9-20", "ИКБО-10-20", "ИКБО-11-20", 
                             "ИКБО-12-20", "ИКБО-13-20", "ИКБО-14-20", "ИКБО-15-20", 
                             "ИКБО-16-20", "ИКБО-17-20", "ИКБО-18-20", "ИКБО-19-20", 
                             "ИКБО-20-20", "ИКБО-21-20", "ИКБО-22-20", "ИКБО-23-20", 
                             "ИКБО-24-20", "ИКБО-24-23", "ИКБО-62-23"]

let students = List (Student) [ { age = 19, group = "ИКБО-4-20", name = "Иванов И.И." }
                               , { age = 18, group = "ИКБО-5-20", name = "Петров П.П." }
                               , { age = 18, group = "ИКБО-5-20", name = "Сидоров С.С." }
                               , { age: 33, group: "ИКБО-62-23", name: "Тревис Скотт" }
                               ]

in { groups = groups, students = students, subject = "Конфигурационное управление" }

```

## Задачи №3-5
Реализовать грамматики, описывающие следующие языки (для каждого решения привести БНФ). Код решения должен содержаться в переменной BNF

## №3 - Язык нулей и единиц

### БНФ
```
E = 0 | 1 | E E
```

### Использование в коде

```Python
BNF = '''
E = 0 | 1 | E E
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'E'))
```
### Примеры вывода
![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/practice3/3-1.jpg) ![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/practice3/3-2.jpg)

## №4 - Язык правильно расставленных скобок двух видов

### БНФ
```
E = () | {} | E E | ( E ) | { E }
```

### Использование в коде

```Python
BNF = '''
E = () | {} | E E | ( E ) | { E }
'''

for i in range(1):
    print(generate_phrase(parse_bnf(BNF), 'E'))
```
### Примеры вывода
![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/practice3/3-3.jpg) ![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/practice3/3-4.jpg) ![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/practice3/3-5.jpg)

## №5 - Язык выражений алгебры логики

### БНФ
```
E  = T | E '|' T                   
T  = F | T '&' F                   
F  = 'x' | 'y' | '~' G | G         
G  = '(' E ')' | 'x' | 'y'
```

### Использование в коде

```Python
BNF = '''
E  = T | E '|' T                   
T  = F | T '&' F                   
F  = 'x' | 'y' | '~' G | G         
G  = '(' E ')' | 'x' | 'y' 
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'E'))
```


### Использование в коде

Получаем вывод без кавычек с помощью метода replace().

```Python
def parse_bnf(text):
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.strip().replace("'","").split() for alt in body.split(' | ')]
    return grammar
```

### Примеры вывода
![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/practice3/3-6.jpg) ![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/practice3/3-7.jpg) ![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/practice3/3-8.jpg)



