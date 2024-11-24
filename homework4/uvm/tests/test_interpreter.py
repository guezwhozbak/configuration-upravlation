import unittest
from interpreter import interpret
import yaml

class TestInterpreter(unittest.TestCase):
    def test_load_const(self):
        input_file = 'examples/tests/test_load_const.bin'
        output_file = 'examples/tests/test_load_const.result'
        memory_range = (0, 256)
        interpret(input_file, output_file, memory_range)
        with open(output_file, 'r') as f:
            result = yaml.safe_load(f)
        self.assertEqual(result[0], 385)

    def test_read_mem(self):
        input_file = 'examples/tests/test_read_mem.bin'
        output_file = 'examples/tests/test_read_mem.result'
        memory_range = (0, 256)
        interpret(input_file, output_file, memory_range)
        with open(output_file, 'r') as f:
            result = yaml.safe_load(f)
        self.assertEqual(result[7], 254)

    def test_write_mem(self):
        input_file = 'examples/tests/test_write_mem.bin'
        output_file = 'examples/tests/test_write_mem.result'
        memory_range = (0, 256)
        interpret(input_file, output_file, memory_range)
        with open(output_file, 'r') as f:
            result = yaml.safe_load(f)
        self.assertEqual(result[3], 0)

    #def test_max(self):
    #    input_file = 'examples/tests/test_max.bin'
    #    output_file = 'examples/tests/test_max.result'
    #    memory_range = (0, 256)
    #    interpret(input_file, output_file, memory_range)
    #    with open(output_file, 'r') as f:
    #        result = yaml.safe_load(f)
    #    self.assertEqual(result[7], 375)

if __name__ == '__main__':
    unittest.main()












