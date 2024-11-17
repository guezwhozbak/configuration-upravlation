import argparse
import os
import sys

# Добавление пути к проекту в PYTHONPATH, переменная PATH содержит список директорий, в которых операционная система ищет исполняемые файлы.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.graph_builder import build_graph

def parse_args():
    # Создание парсера аргументов командной строки
    parser = argparse.ArgumentParser(description='Visualize git commit dependencies.')
    parser.add_argument('--graphviz_path', required=True, help='Path to Graphviz executable.')
    parser.add_argument('--repo_path', required=True, help='Path to the git repository.')
    parser.add_argument('--date', required=True, help='Date to filter commits (YYYY-MM-DD).')
    # Возврат объекта с распарсенными аргументамиreturn parser.parse_args()

def main():
    # Получение аргументов командной строки
    args = parse_args()
    graphviz_path = args.graphviz_path

    # Добавление пути к Graphviz в переменную окружения PATH
    os.environ["PATH"] += os.pathsep + graphviz_path
    # Построение графа
    dot = build_graph(args.repo_path, args.date)
    dot.render('commit_graph', format='png', view=True)

if __name__ == '__main__':
    main()