import sys  # Импортируем модуль sys для работы с аргументами командной строки
import yaml  # Импортируем модуль yaml для работы с YAML-файлами

def assemble(input_file, output_file, log_file):
    # Чтение исходного файла
    with open(input_file, 'r') as f:
        lines = f.readlines()  # Читаем все строки из файла

    # Парсинг команд и генерация бинарного файла
    binary_data = []  # Список для хранения бинарных данных
    log_data = []  # Список для хранения логов
    for line in lines:
        parts = line.strip().split()  # Разделяем строку на части, удаляя пробелы
        if not parts:
            continue  # Пропускаем пустые строки
        if parts[0] == 'LOAD_CONST':
            if len(parts) < 3:
                raise ValueError(f"Недостаточно аргументов для команды LOAD_CONST в строке: {line}")
            A = 29  # Код команды LOAD_CONST
            B = int(parts[1])  # Первый аргумент команды
            C = int(parts[2])  # Второй аргумент команды
            binary_data.append(0x3D)  # Опкод команды LOAD_CONST
            binary_data.append((B >> 8) & 0xFF)  # Старший байт B
            binary_data.append(B & 0xFF)  # Младший байт B
            binary_data.append(C)  # Адрес регистра C
            log_data.append({'A': A, 'B': B, 'C': C})  # Добавляем лог команды
        elif parts[0] == 'READ_MEM':
            if len(parts) < 3:
                raise ValueError(f"Недостаточно аргументов для команды READ_MEM в строке: {line}")
            A = 6  # Код команды READ_MEM
            B = int(parts[1])  # Первый аргумент команды
            C = int(parts[2])  # Второй аргумент команды
            binary_data.append(0xE6)  # Опкод команды READ_MEM
            binary_data.append(B)  # Адрес регистра B
            binary_data.append((C >> 16) & 0xFF)  # Старший байт C
            binary_data.append((C >> 8) & 0xFF)  # Средний байт C
            binary_data.append(C & 0xFF)  # Младший байт C
            log_data.append({'A': A, 'B': B, 'C': C})  # Добавляем лог команды
        elif parts[0] == 'WRITE_MEM':
            if len(parts) < 3:
                raise ValueError(f"Недостаточно аргументов для команды WRITE_MEM в строке: {line}")
            A = 3  # Код команды WRITE_MEM
            B = int(parts[1])  # Первый аргумент команды
            C = int(parts[2])  # Второй аргумент команды
            binary_data.append(0x03)  # Опкод команды WRITE_MEM
            binary_data.append(B)  # Адрес регистра B
            binary_data.append(C)  # Адрес регистра C
            log_data.append({'A': A, 'B': B, 'C': C})  # Добавляем лог команды
        elif parts[0] == 'MAX':
            if len(parts) < 3:
                raise ValueError(f"Недостаточно аргументов для команды MAX в строке: {line}")
            A = 27  # Код команды MAX
            B = int(parts[1])  # Первый аргумент команды
            C = int(parts[2])  # Второй аргумент команды
            if B >= 256 or C >= 256:
                raise ValueError(f"Значение B={B} или C={C} выходит за пределы допустимого диапазона")
            binary_data.append(0xFB)  # Опкод команды MAX
            binary_data.append((B >> 16) & 0xFF)  # Старший байт B
            binary_data.append((B >> 8) & 0xFF)  # Средний байт B
            binary_data.append(B & 0xFF)  # Младший байт B
            binary_data.append(C)  # Адрес регистра C
            log_data.append({'A': A, 'B': B, 'C': C})  # Добавляем лог команды
        else:
            raise ValueError(f"Неизвестная команда в строке: {line}")

    # Запись бинарного файла
    with open(output_file, 'wb') as f:
        f.write(bytearray(binary_data))  # Записываем бинарные данные в файл

    # Запись лога
    with open(log_file, 'w') as f:
        yaml.dump(log_data, f)  # Записываем логи в YAML-файл

if __name__ == "__main__":
    input_file = sys.argv[1]  # Получаем имя входного файла из аргументов командной строки
    output_file = sys.argv[2]  # Получаем имя выходного файла из аргументов командной строки
    log_file = sys.argv[3]  # Получаем имя лог-файла из аргументов командной строки
    assemble(input_file, output_file, log_file)  # Вызываем функцию assemble
















