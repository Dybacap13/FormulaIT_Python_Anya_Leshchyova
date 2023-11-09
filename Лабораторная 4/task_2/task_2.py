# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    result_list = []
    with open(INPUT_FILENAME, 'r') as file:
        reader = csv.DictReader(file, delimiter=',', quotechar='\n')
        for row in reader:
            result_list.append(row)
    with open(OUTPUT_FILENAME, 'w') as f:
        json.dump(result_list, f, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
