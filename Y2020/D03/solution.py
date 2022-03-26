
#' Part 1: Done
#' Part 2: Done

import sys
sys.path.insert(0,".")
from AoCDecorator import AoC

def checkslope(data,right,down):

    data2 = data[0::down]

    W = len(data2[0])
    H = len(data2)
    pattern = [x % W for x in range(0,right*W,right)]
    pattern2 = ((H//W + 1)*pattern)[0:H]

    trees = [x[p] == '#' for x,p in zip(data2,pattern2)]

    return sum(trees)

@AoC(2020,3)
def solve(data,part):
    if part == 1:
        return checkslope(data,3,1)
    if part == 2:
        slopes = [
            {"right":1,"down":1},
            {"right":3,"down":1},
            {"right":5,"down":1},
            {"right":7,"down":1},
            {"right":1,"down":2},
        ]
        out = 1
        for x in slopes:
            out *= checkslope(data,**x)
        return out


if(__name__ == "__main__"):
    solve()
