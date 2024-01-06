import functools
import re


with open(r'input.txt', "r") as f:
    lines = f.read().splitlines()


cards = [[set(re.findall(r'\d+', side)) for side in line.split(':')[1].split('|')] for line in lines]
n_wins = [len(have.intersection(want)) for have, want in cards]
answer1 = sum(2**(n - 1) for n in n_wins if n > 0)
print(answer1)


# Part 2
@functools.cache
def count_scratchcards(i):
  if i > len(n_wins):
    return 0
  return 1 + sum(count_scratchcards(i + j + 1) for j in range(n_wins[i]))


answer2 = sum(count_scratchcards(i) for i in range(len(n_wins)))
print(answer2)
