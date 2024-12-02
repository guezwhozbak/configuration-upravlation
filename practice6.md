# Практическое занятие №6 "Системы автоматизации сборки"
Выполнила **Рожкова Ольга**, группа **ИКБО-62-23** 
---
## Задача №1

Написать программу на Питоне, которая транслирует граф зависимостей civgraph в makefile в духе примера выше. Для мало знакомых с Питоном используется упрощенный вариант civgraph: civgraph.json.

### Решение

Файл generate_makefile.py:
```py
import json

def generate_makefile(dependencies):
    makefile_content = []

    for target, deps in dependencies.items():
        if deps:
            makefile_content.append(f"{target}: {' '.join(deps)}")
            makefile_content.append(f"\t@echo \"{target} depends on {' and '.join(deps)}\"")
        else:
            makefile_content.append(f"{target}:")
            makefile_content.append(f"\t@echo \"{target} has no dependencies\"")

    return "\n".join(makefile_content)

def main():
    with open('civgraph.json', 'r') as file:
        dependencies = json.load(file)

    makefile_content = generate_makefile(dependencies)

    with open('Makefile', 'w') as file:
        file.write(makefile_content)

if __name__ == "__main__":
    main()
```
civgraph.json:
```json
{
    "mathematics": ["astrology", "celestial_navigation"],
    "astrology": ["mysticism"],
    "celestial_navigation": ["sailing"],
    "sailing": ["foreign_trade"],
    "foreign_trade": ["currency"],
    "currency": [],
    "mysticism": [],
    "mining": [],
    "bronze_working": ["mining"],
    "pottery": [],
    "writing": [],
    "code_of_laws": ["writing"],
    "irrigation": [],
    "masonry": [],
    "early_empire": ["code_of_laws", "masonry"],
    "drama_poetry": ["writing"]
}
```
makefile:
```make
mathematics: astrology celestial_navigation
	@echo "mathematics depends on astrology and celestial_navigation"
astrology: mysticism
	@echo "astrology depends on mysticism"
celestial_navigation: sailing
	@echo "celestial_navigation depends on sailing"
sailing: foreign_trade
	@echo "sailing depends on foreign_trade"
foreign_trade: currency
	@echo "foreign_trade depends on currency"
currency:
	@echo "currency has no dependencies"
mysticism:
	@echo "mysticism has no dependencies"
mining:
	@echo "mining has no dependencies"
bronze_working: mining
	@echo "bronze_working depends on mining"
pottery:
	@echo "pottery has no dependencies"
writing:
	@echo "writing has no dependencies"
code_of_laws: writing
	@echo "code_of_laws depends on writing"
irrigation:
	@echo "irrigation has no dependencies"
masonry:
	@echo "masonry has no dependencies"
early_empire: code_of_laws masonry
	@echo "early_empire depends on code_of_laws and masonry"
drama_poetry: writing
	@echo "drama_poetry depends on writing"
```
Выполнение команды **make** для проверки работоспособности: 

![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/practice6/6-1.jpg)

## Задача №2

Реализовать вариант трансляции, при котором повторный запуск make не выводит для civgraph на экран уже выполненные "задачи".

### Решение

Изменённый generate_makefile.py:
```py
import json
import os

def generate_makefile(dependencies):
    makefile_content = []

    for target, deps in dependencies.items():
        if deps:
            # добавлено расширение .done для целей и зависимостей
            makefile_content.append(f"{target}.done: {' '.join([dep + '.done' for dep in deps])}")
            makefile_content.append(f"\t@echo \"{target} depends on {' and '.join(deps)}\"")
            # команда touch для создания временного файла
            makefile_content.append(f"\ttouch {target}.done")
        else:
            # добавлено расширение .done для целей
            makefile_content.append(f"{target}.done:")
            makefile_content.append(f"\t@echo \"{target} has no dependencies\"")
            # команда touch для создания временного файла
            makefile_content.append(f"\ttouch {target}.done")

    return "\n".join(makefile_content)

def main():
    with open('civgraph.json', 'r') as file:
        dependencies = json.load(file)

    makefile_content = generate_makefile(dependencies)

    with open('Makefile', 'w') as file:
        file.write(makefile_content)

if __name__ == "__main__":
    main()
```
Новый makefile:
```make
mathematics.done: astrology.done celestial_navigation.done
	@echo "mathematics depends on astrology and celestial_navigation"
	touch mathematics.done
astrology.done: mysticism.done
	@echo "astrology depends on mysticism"
	touch astrology.done
celestial_navigation.done: sailing.done
	@echo "celestial_navigation depends on sailing"
	touch celestial_navigation.done
sailing.done: foreign_trade.done
	@echo "sailing depends on foreign_trade"
	touch sailing.done
foreign_trade.done: currency.done
	@echo "foreign_trade depends on currency"
	touch foreign_trade.done
currency.done:
	@echo "currency has no dependencies"
	touch currency.done
mysticism.done:
	@echo "mysticism has no dependencies"
	touch mysticism.done
mining.done:
	@echo "mining has no dependencies"
	touch mining.done
bronze_working.done: mining.done
	@echo "bronze_working depends on mining"
	touch bronze_working.done
pottery.done:
	@echo "pottery has no dependencies"
	touch pottery.done
writing.done:
	@echo "writing has no dependencies"
	touch writing.done
code_of_laws.done: writing.done
	@echo "code_of_laws depends on writing"
	touch code_of_laws.done
irrigation.done:
	@echo "irrigation has no dependencies"
	touch irrigation.done
masonry.done:
	@echo "masonry has no dependencies"
	touch masonry.done
early_empire.done: code_of_laws.done masonry.done
	@echo "early_empire depends on code_of_laws and masonry"
	touch early_empire.done
drama_poetry.done: writing.done
	@echo "drama_poetry depends on writing"
	touch drama_poetry.done
```
Выполнение команды **make** для проверки работоспособности: 

![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/practice6/6-2.jpg)

## Задача №3

Добавить цель clean, не забыв и про "животное".

### Решение

Изменённый generate_makefile.py
```py
import json
import os

def generate_makefile(dependencies):
    makefile_content = []

    # Добавляем цель all
    all_targets = list(dependencies.keys())
    makefile_content.append(f"all: {' '.join([target + '.done' for target in all_targets])}")
    makefile_content.append("\t@echo \"All done. Let's go outside!\"")

    # Добавляем цель clean
    makefile_content.append("clean:")
    makefile_content.append("\trm -f *.done")
    makefile_content.append("\t@echo \"Cleaned up all temporary files.\"")

    for target, deps in dependencies.items():
        if deps:
            makefile_content.append(f"{target}.done: {' '.join([dep + '.done' for dep in deps])}")
            makefile_content.append(f"\t@echo \"{target} depends on {' and '.join(deps)}\"")
            makefile_content.append(f"\ttouch {target}.done")
        else:
            makefile_content.append(f"{target}.done:")
            makefile_content.append(f"\t@echo \"{target} has no dependencies\"")
            makefile_content.append(f"\ttouch {target}.done")

    return "\n".join(makefile_content)

def main():
    with open('civgraph.json', 'r') as file:
        dependencies = json.load(file)

    makefile_content = generate_makefile(dependencies)

    with open('Makefile', 'w') as file:
        file.write(makefile_content)

if __name__ == "__main__":
    main()
```
Новый makefile: 
```make
all: mathematics.done astrology.done celestial_navigation.done sailing.done foreign_trade.done currency.done mysticism.done mining.done bronze_working.done pottery.done writing.done code_of_laws.done irrigation.done masonry.done early_empire.done drama_poetry.done
	@echo "All done. Let's go outside!"
clean:
	rm -f *.done
	@echo "Cleaned up all temporary files."
mathematics.done: astrology.done celestial_navigation.done
	@echo "mathematics depends on astrology and celestial_navigation"
	touch mathematics.done
astrology.done: mysticism.done
	@echo "astrology depends on mysticism"
	touch astrology.done
celestial_navigation.done: sailing.done
	@echo "celestial_navigation depends on sailing"
	touch celestial_navigation.done
sailing.done: foreign_trade.done
	@echo "sailing depends on foreign_trade"
	touch sailing.done
foreign_trade.done: currency.done
	@echo "foreign_trade depends on currency"
	touch foreign_trade.done
currency.done:
	@echo "currency has no dependencies"
	touch currency.done
mysticism.done:
	@echo "mysticism has no dependencies"
	touch mysticism.done
mining.done:
	@echo "mining has no dependencies"
	touch mining.done
bronze_working.done: mining.done
	@echo "bronze_working depends on mining"
	touch bronze_working.done
pottery.done:
	@echo "pottery has no dependencies"
	touch pottery.done
writing.done:
	@echo "writing has no dependencies"
	touch writing.done
code_of_laws.done: writing.done
	@echo "code_of_laws depends on writing"
	touch code_of_laws.done
irrigation.done:
	@echo "irrigation has no dependencies"
	touch irrigation.done
masonry.done:
	@echo "masonry has no dependencies"
	touch masonry.done
early_empire.done: code_of_laws.done masonry.done
	@echo "early_empire depends on code_of_laws and masonry"
	touch early_empire.done
drama_poetry.done: writing.done
	@echo "drama_poetry depends on writing"
	touch drama_poetry.done
```
Проверка работоспобности all и clean:

![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/practice6/6-3.jpg)

![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/practice6/6-4.jpg)

## Задача 4

Написать makefile для следующего скрипта сборки:
```
gcc prog.c data.c -o prog
dir /B > files.lst
7z a distr.zip *.*
```
Вместо gcc можно использовать другой компилятор командной строки, но на вход ему должны подаваться два модуля: prog и data. Если используете не Windows, то исправьте вызовы команд на их эквиваленты из вашей ОС. В makefile должны быть, как минимум, следующие задачи: all, clean, archive. Обязательно покажите на примере, что уже сделанные подзадачи у вас не перестраиваются.

### Решение

Makefile:
```make
# Компилятор
CC = gcc

# Исходные файлы
SRC = prog.c data.c

# Объектные файлы
OBJ = prog.o data.o

# Исполняемый файл
TARGET = prog.exe

# Архив
ARCHIVE = distr.zip

# Список файлов
FILES_LIST = files.lst

# Цель all
all: $(TARGET) $(FILES_LIST) $(ARCHIVE)
	@echo "All done. Let's go outside!"

# Цель для компиляции
$(TARGET): $(OBJ)
	$(CC) $(OBJ) -o $(TARGET)

# Цель для создания объектных файлов
%.o: %.c
	$(CC) -c $< -o $@

# Цель для создания списка файлов
$(FILES_LIST):
	@echo "Creating file list..."
	ls > $(FILES_LIST)

# Цель для создания архива
$(ARCHIVE): $(TARGET) $(FILES_LIST)
	@echo "Creating archive..."
	7z a $(ARCHIVE) *.*

# Цель для очистки
clean:
	rm -f $(OBJ) $(TARGET) $(FILES_LIST) $(ARCHIVE)
	@echo "Cleaned up all temporary files."

# Цель для создания архива
archive: $(ARCHIVE)
	@echo "Archive created: $(ARCHIVE)"

# PHONY цели
.PHONY: all clean archive
```
Проверка работоспособности all, clean, archive:

![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/practice6/6-5.jpg)

![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/practice6/6-6.jpg)

![image](https://github.com/guezwhozbak/configuration-upravlation/blob/main/practice6/6-7.jpg)

