
#' Part 1: Done
#' Part 2: Done

import numpy as np

import sys
sys.path.insert(0,".")
from AoCDecorator import AoC

def getdiff(data,n):
    assert isinstance(data,np.ndarray)
    return data[n:] - data[:len(data)-n]

@AoC(2021,1)
def solve(data,part):
    data2 = np.asarray(data).astype(int)
    if part == 1:
        return sum(getdiff(data2,1) >0)
    elif part == 2:
        return sum(getdiff(data2,3) >0)

if(__name__ == "__main__"):
    solve()

#Answer to Part 1: 1557
#Answer to Part 2: 1608