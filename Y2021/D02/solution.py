
#' Part 1: Done
#' Part 2: Done

import numpy as np

import sys
sys.path.insert(0,'.')
from AoCDecorator import AoC

def getif(command,direction):
    d,a = command.split(" ")

    if(d == direction):
        return int(a)
    else:
        return 0

def getifall(data,direction):
    return [getif(x,direction) for x in data]

@AoC(2021,2)
def solve(data,part):
    f_amt = getifall(data,"forward")
    u_amt = getifall(data,"up")
    d_amt = getifall(data,"down")

    l = len(data)-1

    h_dist = sum(f_amt)

    if part == 1:
        v_dist = (sum(d_amt) - sum(u_amt))
    if part == 2:
        aim_amt = np.array(d_amt) - np.array(u_amt)
        v_dist = sum(np.cumsum(aim_amt)*f_amt)
        
    return v_dist*h_dist

if(__name__ == '__main__'):
    solve()

# Answer 1: 1936494
# Answer 2: 1997106066