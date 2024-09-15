# Практическое занятие №1
## Задача 1
Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd.
### Код
```
grep '^[^:]*' /etc/passwd | cut -d: -f1 | sort
```
### Вывод
![image](https://github.com/guezwhozbak/cfg/blob/main/practice1/1.jpg)

## Задача 2
Вывести данные /etc/protocols в отформатированном и отсортированном порядке для 5 наибольших портов.
### Код
```
cat /etc/protocols | awk '{print $2, $1}' | sort -nr | head -n 5
```
### Вывод
![image](https://github.com/guezwhozbak/cfg/blob/main/practice1/2.jpg)

## Задача 3
Написать программу banner средствами bash для вывода текстов.
### Код на Python
```
x = input()
print('+', end="")
y = [print('-', end="") for i in range(len(x) + 2)]
print('+')
print(f"| {x} |")
print('+', end="")
y = [print('-', end='') for i in range(len(x) + 2)]
print("+")
```
### Вывод
![image](https://github.com/guezwhozbak/cfg/blob/main/practice1/3.jpg)

## Задача 1
Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd.
### Код
```
grep '^[^:]*' /etc/passwd | cut -d: -f1 | sort
```
### Вывод
![image](https://github.com/guezwhozbak/cfg/blob/main/practice1/1.jpg)

## Задача 1
Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd.
### Код
```
grep '^[^:]*' /etc/passwd | cut -d: -f1 | sort
```
### Вывод
![image](https://github.com/guezwhozbak/cfg/blob/main/practice1/1.jpg)

## Задача 1
Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd.
### Код
```
grep '^[^:]*' /etc/passwd | cut -d: -f1 | sort
```
### Вывод
![image](https://github.com/guezwhozbak/cfg/blob/main/practice1/1.jpg)

## Задача 1
Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd.
### Код
```
grep '^[^:]*' /etc/passwd | cut -d: -f1 | sort
```
### Вывод
![image](https://github.com/guezwhozbak/cfg/blob/main/practice1/1.jpg)

## Задача 1
Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd.
### Код
```
grep '^[^:]*' /etc/passwd | cut -d: -f1 | sort
```
### Вывод
![image](https://github.com/guezwhozbak/cfg/blob/main/practice1/1.jpg)

## Задача 1
Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd.
### Код
```
grep '^[^:]*' /etc/passwd | cut -d: -f1 | sort
```
### Вывод
![image](https://github.com/guezwhozbak/cfg/blob/main/practice1/1.jpg)

## Задача 1
Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd.
### Код
```
grep '^[^:]*' /etc/passwd | cut -d: -f1 | sort
```
### Вывод
![image](https://github.com/guezwhozbak/cfg/blob/main/practice1/1.jpg)


