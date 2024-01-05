import math
import re


with open(r'input.txt', "r") as f:
    lines = f.readlines()


numbers = {}
symbols = {}
for row, line in enumerate(lines):
    for match in re.finditer(r'\d+', line):
        for col in range(match.start(), match. end()):
            numbers[(row, col)] = match
    for match in re.finditer(r'[^0-9.\n]', line):
        symbols[(row, match.start())] = [match.group()]

for (row, col), l in symbols.items():
    neighbours = {numbers[(row + dr, col + dc)] for dr in range(-1, 2) for dc in range(-1, 2) if (row + dr, col + dc) in numbers}
    l.append([int(match.group()) for match in neighbours])

answer1 = sum(num for _, neighbours in symbols.values() for num in neighbours)
print(answer1)


# Part 2
answer2 = sum(math.prod(nums) for symbol, nums in symbols.values() if symbol == '*' and len(nums) == 2)
print(answer2)
