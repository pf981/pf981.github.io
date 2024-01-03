import math
import re


with open('input.txt', "r") as f:
    lines = f.readlines()


def extract_cubes(line):
    return [extract_max(line, color) for color in ['red', 'green', 'blue']]


def extract_max(line, c):
    return max(int(num) for num in re.findall(r'(\d+) ' + c, line))


max_cubes = [extract_cubes(line) for line in lines]
answer1 = sum(i for i, cubes in enumerate(max_cubes, 1) if cubes[0] <= 12 and cubes[1] <= 13 and cubes[2] <= 14)
print(answer1)


# Part 2
answer2 = sum(math.prod(cubes) for cubes in max_cubes)
print(answer2)
