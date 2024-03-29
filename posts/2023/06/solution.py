import math
import re


with open('input.txt', "r") as f:
    lines = f.readlines()


def count_ways(T, D):
    #     D = w * (T - w)
    # =>  0 = -w**2 + T*w - D
    # =>  zeroes at (-T +- sqrt(T**2 - 4*(-1)*(-D))) / 2*(-1)  (quadratic formula)
    upper = (-T - math.sqrt(T ** 2 - 4 * (-1) * (-D))) / 2 * (-1)
    lower = (-T + math.sqrt(T ** 2 - 4 * (-1) * (-D))) / 2 * (-1)
    return math.ceil(upper) - math.floor(lower) - 1


times, distances = [[int(x) for x in re.findall(r'\d+', line)] for line in lines]
answer1 = math.prod(count_ways(time, distance) for time, distance in zip(times, distances))
print(answer1)


# Part 2
time, distance = [int(''.join(str(x) for x in dim)) for dim in [times, distances]]
answer2 = count_ways(time, distance)
print(answer2)
