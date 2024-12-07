# Практическое занятие №7 "Генераторы документации"
Выполнила **Рожкова Ольга**, группа **ИКБО-62-23** 
---
## Задача №1

Реализовать с помощью математического языка LaTeX формулу. Прислать код на LaTeX и картинку-результат, где, помимо формулы, будет указано ФИО студента.

### Решение

Код на LaTeX: 

```latex
\documentclass{article}
\usepackage{amsmath}
\usepackage[utf8]{inputenc}
\usepackage[russian]{babel}

\begin{document}

Рожкова Ольга Сергеевна

\[
\int_{x}^{\infty} \frac{dt}{t(t^{2}-1) \log t} = \int_{x}^{\infty} \frac{1}{t \log t} \left( \sum_{m} t^{-2m} \right) dt = \sum_{m} \int_{x}^{\infty} \frac{t^{-2m}}{t \log t} dt \quad (u = t^{-2m}) = -\sum_{m} \operatorname{li}(x^{-2m})
\]

\end{document}
```
Полученная формула:

![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/practice7/7-1.jpg)

## Задача №2

На языке PlantUML реализовать диаграмму на рисунке ниже. Прислать текст на PlantUML и картинку-результат, в которой ФИО студента заменены Вашими собственными. Обратите внимание на оформление, желательно придерживаться именно его, то есть без стандартного желтого цвета и проч. Чтобы много не писать используйте псевдонимы с помощью ключевого слова "as".

### Решение

Код на PlantUML:

```plantuml
@startuml
actor "Рожкова Ольга Сергеевна" as Студент
database "Piazza" as Piazza
actor "Преподаватель" as Преподаватель

Преподаватель -> Piazza : Публикация задачи
activate Piazza
Piazza --> Преподаватель : Задача опубликована
deactivate Piazza

Студент -> Piazza : Поиск задач
activate Piazza
Piazza --> Студент : Получение задачи
deactivate Piazza

Студент -> Piazza : Публикация решения
activate Piazza
Piazza --> Студент : Решение опубликовано
deactivate Piazza

Преподаватель -> Piazza : Поиск решений
activate Piazza
Piazza --> Преподаватель : Решение найдено
Преподаватель -> Piazza : Публикация оценки
Piazza --> Преподаватель : Оценка опубликована
deactivate Piazza

Студент -> Piazza : Проверка оценки
activate Piazza
Piazza --> Студент : Оценка получена
deactivate Piazza

@enduml
```
Полученное изображение:

![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/practice7/7-2.jpg)





