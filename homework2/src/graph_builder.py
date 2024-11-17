from git import Repo
from graphviz import Digraph
from datetime import datetime, timezone

def build_graph(repo_path, date):
    repo = Repo(repo_path)
    commits = list(repo.iter_commits())
    filter_date = datetime.strptime(date, '%Y-%m-%d').replace(tzinfo=timezone.utc)
    filtered_commits = [commit for commit in commits if commit.committed_datetime < filter_date]

    # Сортировка коммитов в хронологическом порядке
    filtered_commits.sort(key=lambda commit: commit.committed_datetime)

    dot = Digraph(comment='Commit Dependencies')
    for commit in filtered_commits:
        dot.node(commit.hexsha, commit.hexsha)
        for parent in commit.parents:
            dot.edge(parent.hexsha, commit.hexsha)

    return dot

