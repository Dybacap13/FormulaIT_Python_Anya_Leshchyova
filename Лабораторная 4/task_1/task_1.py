import json
INPUT_FILE = "input.json"

def task() -> float:
    sum_ = 0.0
    with open(INPUT_FILE, 'r') as file:
        data = json.load(file)
    for i in data:
        sum_ += i["score"] * i["weight"]
    return round(sum_, 3)

print(task())
