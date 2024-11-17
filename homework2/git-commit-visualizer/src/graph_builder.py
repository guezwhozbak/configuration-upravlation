import subprocess
from graphviz import Digraph
from datetime import datetime, timezone

def get_commits(repo_path, date):
    # Преобразование строки даты в объект datetime с временной зоной UTC
    filter_date = datetime.strptime(date, '%Y-%m-%d').replace(tzinfo=timezone.utc)
    commits = []

    # Выполнение команды git log для получения информации о коммитах
    result = subprocess.run(['git', '-C', repo_path, 'log', '--pretty=format:%H %ct', '--before', date], capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Error running git log: {result.stderr}")

    # Обработка вывода команды git log
    for line in result.stdout.splitlines():
        # Разделение строки на хеш коммита и время коммита
        commit_hash, commit_time = line.split()
        # Преобразование времени коммита в объект datetime
        commit_time = datetime.fromtimestamp(int(commit_time), timezone.utc)
        if commit_time < filter_date:
            commits.append((commit_hash, commit_time))

    # Возврат списка коммитов
    return commits

def build_graph(repo_path, date):
    commits = get_commits(repo_path, date)
    commits.sort(key=lambda x: x[1])  # Сортировка коммитов по времени

    # Создание объекта графа
    dot = Digraph(comment='Commit Dependencies')
    for commit_hash, _ in commits:
        dot.node(commit_hash, commit_hash)

        # Получение родительских коммитов
        result = subprocess.run(['git', '-C', repo_path, 'log', '-1', '--pretty=format:%P', commit_hash], capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f"Error running git log: {result.stderr}")

        # Разделение строки родительских хешей на отдельные хеши
        parents = result.stdout.strip().split()
        for parent in parents:
            # Добавление ребра в граф от родительского коммита к текущему коммиту
            dot.edge(parent, commit_hash)

    # Возврат объекта графа
    return dot



