import sys  # Импортируем модуль sys для работы с аргументами командной строки
import yaml  # Импортируем модуль yaml для работы с YAML-файлами

def interpret(input_file, output_file, memory_range):
    # Чтение бинарного файла
    with open(input_file, 'rb') as f:
        binary_data = f.read()  # Читаем бинарные данные из файла

    # Инициализация памяти
    memory = [0] * 256  # Создаем массив памяти размером 256 байт

    # Выполнение команд
    i = 0  # Инициализируем индекс для обхода бинарных данных
    while i < len(binary_data):
        A = binary_data[i]  # Получаем опкод команды
        if A == 0x3D:  # LOAD_CONST
            B = (binary_data[i+1] << 8) | binary_data[i+2]  # Получаем значение B
            C = binary_data[i+3]  # Получаем адрес регистра C
            if C >= len(memory):
                raise IndexError(f"Индекс вне диапазона: C={C}")
            memory[C] = B  # Записываем значение B в регистр C
            i += 4  # Переходим к следующей команде
        elif A == 0xE6:  # READ_MEM
            B = binary_data[i+1]  # Получаем адрес регистра B
            C = (binary_data[i+2] << 16) | (binary_data[i+3] << 8) | binary_data[i+4]  # Получаем адрес регистра C
            if B >= len(memory) or C >= len(memory):
                raise IndexError(f"Индекс вне диапазона: B={B}, C={C}")
            memory[B] = memory[C]  # Копируем значение из регистра C в регистр B
            i += 5  # Переходим к следующей команде
        elif A == 0x03:  # WRITE_MEM
            B = binary_data[i+1]  # Получаем адрес регистра B
            C = binary_data[i+2]  # Получаем адрес регистра C
            if B >= len(memory) or C >= len(memory):
                raise IndexError(f"Индекс вне диапазона: B={B}, C={C}")
            memory[C] = memory[B]  # Копируем значение из регистра B в регистр C
            i += 3  # Переходим к следующей команде
        elif A == 0xFB:  # MAX
            B = (binary_data[i+1] << 16) | (binary_data[i+2] << 8) | binary_data[i+3]  # Получаем значение B
            C = binary_data[i+4]  # Получаем адрес регистра C
            if B >= len(memory) or C >= len(memory):
                raise IndexError(f"Индекс вне диапазона: B={B}, C={C}")
            memory[C] = max(memory[C], memory[B])  # Записываем максимальное значение в регистр C
            i += 5  # Переходим к следующей команде
        else:
            raise ValueError(f"Неизвестная команда в байте: {A}")

    # Запись результата
    result = memory[memory_range[0]:memory_range[1]]  # Получаем диапазон памяти для записи
    with open(output_file, 'w') as f:
        yaml.dump(result, f)  # Записываем результат в YAML-файл

if __name__ == "__main__":
    input_file = sys.argv[1]  # Получаем имя входного файла из аргументов командной строки
    output_file = sys.argv[2]  # Получаем имя выходного файла из аргументов командной строки
    memory_range = (int(sys.argv[3]), int(sys.argv[4]))  # Получаем диапазон памяти из аргументов командной строки
    interpret(input_file, output_file, memory_range)  # Вызываем функцию interpret













