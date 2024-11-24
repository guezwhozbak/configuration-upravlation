import unittest
from assembler import assemble
import yaml

class TestAssembler(unittest.TestCase):
    def test_load_const(self):
        input_file = 'examples/tests/test_load_const.asm'
        output_file = 'examples/tests/test_load_const.bin'
        log_file = 'examples/tests/test_load_const.log'
        assemble(input_file, output_file, log_file)
        with open(log_file, 'r') as f:
            log_data = yaml.safe_load(f)
        self.assertEqual(log_data, [{'A': 29, 'B': 385, 'C': 0}])

    def test_read_mem(self):
        input_file = 'examples/tests/test_read_mem.asm'
        output_file = 'examples/tests/test_read_mem.bin'
        log_file = 'examples/tests/test_read_mem.log'
        assemble(input_file, output_file, log_file)
        with open(log_file, 'r') as f:
            log_data = yaml.safe_load(f)
        self.assertEqual(log_data, [{'A': 29, 'B': 254, 'C': 254}, {'A': 6, 'B': 7, 'C': 254}])

    def test_write_mem(self):
        input_file = 'examples/tests/test_write_mem.asm'
        output_file = 'examples/tests/test_write_mem.bin'
        log_file = 'examples/tests/test_write_mem.log'
        assemble(input_file, output_file, log_file)
        with open(log_file, 'r') as f:
            log_data = yaml.safe_load(f)
        self.assertEqual(log_data, [{'A': 29, 'B': 0, 'C': 0}, {'A': 3, 'B': 0, 'C': 3}])

    #def test_max(self):
    #    input_file = 'examples/tests/test_max.asm'
    #    output_file = 'examples/tests/test_max.bin'
    #    log_file = 'examples/tests/test_max.log'
    #    assemble(input_file, output_file, log_file)
    #    with open(log_file, 'r') as f:
    #        log_data = yaml.safe_load(f)
    #    self.assertEqual(log_data, [{'A': 29, 'B': 375, 'C': 7}, {'A': 29, 'B': 375, 'C': 375}, {'A': 27, 'B': 7, 'C': 7}])

if __name__ == '__main__':
    unittest.main()













