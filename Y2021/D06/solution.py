
#' Part 1: Done
#' Part 2: Done

import sys
sys.path.insert(0,".")
from AoCDecorator import AoC

def next_step(cyl):
    zero = cyl[0]
    cyl = cyl[1:] + [0]
    cyl[8] += zero
    cyl[6] += zero
    #print(cyl)
    return cyl

@AoC(2021,6)
def solve(data,part):

    if part == 1:
        days = 80
    if part == 2:
        days = 256
    
    data2 = [int(x) for x in data[0].split(",")]
    lcyl = [0]*9

    for i in data2:
        lcyl[i] += 1

    for i in range(0,days):
        lcyl = next_step(lcyl)
    
    return sum(lcyl)



if(__name__ == "__main__"):
    solve()
