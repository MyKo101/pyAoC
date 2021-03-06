
import re

import sys
sys.path.insert(0,".")
from AoCDecorator import AoC

def row_to_dict(x):
    return {
        "min": int(x[0]),
        "max": int(x[1]),
        "letter": x[2],
        "password": x[3]
    }

def checkrow1(min,max,letter,password):
    count = int(password.count(letter))
    return min <=count <= max

def checkrow2(min,max,letter,password):
    return (password[min-1] == letter) != (password[max-1] == letter)

@AoC(2020,2)
def solve(data,part):
    pattern = re.compile("^([0-9]*)-([0-9]*) ([a-z]): ([a-z]*)$")
    data2 = [list(pattern.findall(x)[0]) for x in data]
    data3 = [row_to_dict(x) for x in data2]
    if part == 1:
        correct = [checkrow1(**x) for x in data3]
    if part == 2:
        correct = [checkrow2(**x) for x in data3]

    return sum(correct)

if(__name__ == "__main__"):
    solve()

# Answer 1: 622
# Answer 2: 263
