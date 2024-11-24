#!/bin/bash

python -m unittest discover -s tests
# Сборка проекта
python -m assembler.assembler examples/max_program.asm examples/max_program.bin examples/max_program.yaml
python -m interpreter.interpreter examples/max_program.bin examples/max_result.yaml 0 255