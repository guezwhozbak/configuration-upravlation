# Практическое занятие №1
## Задача 1
Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd.
### Код
```
grep '^[^:]*' /etc/passwd | cut -d: -f1 | sort
```
### Вывод
![image](https://github.com/guezwhozbak/cfg/edit/main/practice1/1.jpg)


