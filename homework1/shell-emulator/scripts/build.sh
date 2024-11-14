#!/bin/bash

# Устанавливаем зависимости
pip install -r requirements.txt

# Запускаем тесты
python -m unittest discover -s tests

# Запускаем эмулятор
python -m src.main --hostname "guezwhozbak" --fs_path "virtual_fs.zip" --log_path "log.xml" --startup_script "scripts/startup_script.sh"
