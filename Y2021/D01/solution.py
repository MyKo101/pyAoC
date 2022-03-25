
import numpy as np
import sys

sys.path.insert(0,".")
from AoCClass import AoC


def getdiff(data,n):
    assert isinstance(data,np.ndarray)
    return data[n:] - data[:len(data)-n]

class solution(AoC):
    year = 2021
    day = 1
    example = ['199', '200', '208', '210', '200', 
                '207','240','269', '260', '263']
    complete = [True,True]

    def solve(self, data, part):
        data2 = np.asarray(data).astype(int)
        if part == 1:
            return sum(getdiff(data2,1) >0)
        elif part == 2:
            return sum(getdiff(data2,3) >0)

if(__name__ == "__main__"):
    solution().Answer()

#Answer to Part 1: 1557
#Answer to Part 2: 1608