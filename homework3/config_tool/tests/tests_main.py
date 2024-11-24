import unittest
import json
import math
from io import StringIO
from unittest.mock import patch
from src.main import convert_dict, evaluate_expression

class TestConfigLanguage(unittest.TestCase):

    def test_convert_dict(self):
        json_input = {
            "name": "John",
            "age": 30,
            "address": {
                "street": "123 Main St",
                "city": "Anytown"
            },
            "constants": {
                "pi": 3.14,
                "expression": ["+", 3.14, 1]
            }
        }
        expected_output = (
            "{\n"
            "  name : @\"John\";\n"
            "  age : 30;\n"
            "  address : {\n"
            "    street : @\"123 Main St\";\n"
            "    city : @\"Anytown\";\n"
            "  };\n"
            "  constants : {\n"
            "    pi : 3.14;\n"
            "    expression : [+, 3.14, 1];\n"
            "  };\n"
            "}"
        )
        self.assertEqual(convert_dict(json_input), expected_output)

    def test_evaluate_expression(self):
        expr = ["+", 3.14, 1]
        self.assertTrue(math.isclose(evaluate_expression(expr), 4.14))

        expr = ["-", 10, 5]
        self.assertTrue(math.isclose(evaluate_expression(expr), 5))

        expr = ["sqrt", 16]
        self.assertTrue(math.isclose(evaluate_expression(expr), 4))

        expr = ["ord", "A"]
        self.assertTrue(math.isclose(evaluate_expression(expr), 65))

    def test_invalid_key(self):
        json_input = {
            "1name": "John"
        }
        with self.assertRaises(ValueError):
            convert_dict(json_input)

    def test_invalid_value_type(self):
        json_input = {
            "name": None
        }
        with self.assertRaises(ValueError):
            convert_dict(json_input)

    def test_main_function(self):
        json_input = json.dumps({
            "name": "John",
            "age": 30,
            "address": {
                "street": "123 Main St",
                "city": "Anytown"
            },
            "constants": {
                "pi": 3.14,
                "expression": ["+", 3.14, 1]
            }
        })
        expected_output = (
            "{\n"
            "  name : @\"John\";\n"
            "  age : 30;\n"
            "  address : {\n"
            "    street : @\"123 Main St\";\n"
            "    city : @\"Anytown\";\n"
            "  };\n"
            "  constants : {\n"
            "    pi : 3.14;\n"
            "    expression : [+, 3.14, 1];\n"
            "  };\n"
            "}"
        )
        with patch('sys.stdin', StringIO(json_input)), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            from src.main import main
            main()
            self.assertEqual(mock_stdout.getvalue(), expected_output + "\n")

if __name__ == '__main__':
    unittest.main()















