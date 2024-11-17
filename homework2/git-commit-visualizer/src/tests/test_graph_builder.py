import unittest
from src.graph_builder import build_graph
from datetime import datetime, timezone

class TestGraphBuilder(unittest.TestCase):
    def setUp(self):
        self.repo_path = r'C:\Users\guezwhozbak\Desktop\graphviz\configuration-upravlation'
        self.date = '2024-11-17'

    def test_build_graph(self):
        dot = build_graph(self.repo_path, self.date)
        # Проверка, что результат не none
        self.assertIsNotNone(dot)
        # Проверка, что длина строки dot.source > 0
        self.assertTrue(len(dot.source) > 0)

if __name__ == '__main__':
    unittest.main()

