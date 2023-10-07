numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8,
           38, -92, -45, 67, 53, 25]
i = 0
while i < len(numbers):
    if (numbers[i] == None):
        numbers[i] =(sum(numbers[:i]) + sum(numbers[i + 1:])) / len (numbers)
    i += 1
print("Измененный список:", numbers)
