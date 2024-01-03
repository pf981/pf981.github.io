import math
import re


with open('input.txt', "r") as f:
    lines = f.readlines()


def extract_cubes(line):
    return [extract_max(line, color) for color in ['red', 'green', 'blue']]


def extract_max(line, c):
    return max(int(num) for num in re.findall(r'(\d+) ' + c, line))


min_cubes = [extract_cubes(line) for line in lines]
answer1 = sum(i * (cubes[0] <= 12 and cubes[1] <= 13 and cubes[2] <= 14) for i, cubes in enumerate(min_cubes, 1))
print(answer1)


# Part 2
answer2 = sum(math.prod(cubes) for cubes in min_cubes)
print(answer2)
