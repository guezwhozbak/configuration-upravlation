import argparse

def replace_spaces_with_tab(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        content = infile.read()

    modified_content = content.replace(' ' * 4, '\t')

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(modified_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Заменить последовательности из 4 пробелов на символ табуляции.")
    parser.add_argument("input_file", help="Путь к входному файлу.")
    parser.add_argument("output_file", help="Путь к выходному файлу.")

    args = parser.parse_args()

    replace_spaces_with_tab(args.input_file, args.output_file)
    print(f"Замена завершена. Результат записан в '{args.output_file}'.")