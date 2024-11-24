import json
import sys
import math

def parse_json(json_str):
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        sys.exit(1)

def convert_value(value, indent=0):
    indent_str = ' ' * (indent * 2)
    if isinstance(value, str):
        return f'@"{value}"'
    elif isinstance(value, int) or isinstance(value, float):
        return str(value)
    elif isinstance(value, dict):
        return convert_dict(value, indent)
    elif isinstance(value, list):
        return convert_list(value, indent)
    else:
        raise ValueError(f"Unsupported value type: {type(value)}")

def convert_dict(d, indent=0):
    indent_str = ' ' * (indent * 2)
    items = []
    for key, value in d.items():
        if not isinstance(key, str) or not key.isidentifier():
            raise ValueError(f"Invalid key: {key}")
        items.append(f"{indent_str}  {key} : {convert_value(value, indent + 1)};")
    return "{\n" + "\n".join(items) + "\n" + indent_str + "}"

def convert_list(lst, indent=0):
    indent_str = ' ' * (indent * 2)
    items = [convert_value(item, indent + 1) if not isinstance(item, str) else item for item in lst]
    return f"[{', '.join(items)}]"

def evaluate_expression(expr):
    if isinstance(expr, (int, float)):
        return expr
    if expr[0] == '+':
        return evaluate_expression(expr[1]) + evaluate_expression(expr[2])
    elif expr[0] == '-':
        return evaluate_expression(expr[1]) - evaluate_expression(expr[2])
    elif expr[0] == 'sqrt':
        return math.sqrt(evaluate_expression(expr[1]))
    elif expr[0] == 'ord':
        return ord(evaluate_expression(expr[1]))
    else:
        return expr

def main():
    json_input = sys.stdin.read()
    data = parse_json(json_input)
    output = convert_dict(data)
    print(output)

if __name__ == "__main__":
    main()












