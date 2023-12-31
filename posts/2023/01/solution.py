with open('input.txt', "r") as f:
    lines = f.readlines()


def first_value(line, m):
  for i, _ in enumerate(line):
    for text, val in m.items():
      if line[i:].startswith(text):
        return val


m = {c: int(c) for c in '123456789'}

answer1 = sum(10 * first_value(line, m) + first_value(line[::-1], m) for line in lines)
print(answer1)


# Part 2
words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
m.update({text: i for i, text in enumerate(words, 1)})
rev_m = {text[::-1]: value for text, value in m.items()}

answer2 = sum(10 * first_value(line, m) + first_value(line[::-1], rev_m) for line in lines)
print(answer2)
