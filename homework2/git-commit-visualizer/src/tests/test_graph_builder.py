import unittest
from src.graph_builder import build_graph
from datetime import datetime, timezone

class TestGraphBuilder(unittest.TestCase):
    def setUp(self):
        self.repo_path = r'C:\Users\guezwhozbak\Desktop\graphviz\configuration-upravlation'
        self.date = '2023-01-01'

    def test_build_graph(self):
        dot = build_graph(self.repo_path, self.date)
        self.assertIsNotNone(dot)
        self.assertTrue(len(dot.source) > 0)

if __name__ == '__main__':
    unittest.main()


