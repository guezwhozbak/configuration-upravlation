import subprocess
from graphviz import Digraph
from datetime import datetime, timezone

def get_commits(repo_path, date):
    filter_date = datetime.strptime(date, '%Y-%m-%d').replace(tzinfo=timezone.utc)
    commits = []

    # Выполнение команды git log для получения информации о коммитах
    result = subprocess.run(['git', '-C', repo_path, 'log', '--pretty=format:%H %ct', '--before', date], capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Error running git log: {result.stderr}")

    for line in result.stdout.splitlines():
        commit_hash, commit_time = line.split()
        commit_time = datetime.fromtimestamp(int(commit_time), timezone.utc)
        if commit_time < filter_date:
            commits.append((commit_hash, commit_time))

    return commits

def build_graph(repo_path, date):
    commits = get_commits(repo_path, date)
    commits.sort(key=lambda x: x[1])  # Сортировка коммитов по времени

    dot = Digraph(comment='Commit Dependencies')
    commit_number = {}

    # Пронумеровать коммиты
    for index, (commit_hash, _) in enumerate(commits, start=1):
        commit_number[commit_hash] = index
        dot.node(str(index), f"{index}\n{commit_hash}")

    # Получение родительских коммитов и добавление ребер
    for commit_hash, _ in commits:
        result = subprocess.run(['git', '-C', repo_path, 'log', '-1', '--pretty=format:%P', commit_hash], capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f"Error running git log: {result.stderr}")

        parents = result.stdout.strip().split()
        for parent in parents:
            if parent in commit_number:
                dot.edge(str(commit_number[parent]), str(commit_number[commit_hash]))

    return dot





