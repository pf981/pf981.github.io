import collections
import itertools
import math
import re


with open("input.txt", "r") as f:
    text = f.read()


def get_steps(pos):
    it = itertools.cycle(instructions)
    steps = 0
    while pos[-1] != "Z":
        pos = m[pos][next(it) == "R"]
        steps += 1

    return steps


instructions, m = text.split("\n\n")
m = {
    pos: (left, right)
    for pos, left, right in [
        re.findall(r"[A-Z0-9]{3}", line) for line in m.splitlines()
    ]
}
answer1 = get_steps("AAA")
print(answer1)


# Part 2
steps = [get_steps(start_pos) for start_pos in m if start_pos[-1] == "A"]
answer2 = math.lcm(*steps)
print(answer2)
