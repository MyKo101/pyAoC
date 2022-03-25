
import numpy as np

import sys
sys.path.insert(0,'.')
from AoCClass import AoC

def getif(command,direction):
    d,a = command.split(" ")

    if(d == direction):
        return int(a)
    else:
        return 0

def getifall(data,direction):
    return [getif(x,direction) for x in data]

class solution(AoC):
    year = 2021
    day = 2
    example = ['forward 5', 'down 5', 'forward 8',
                'up 3', 'down 8', 'forward 2']
    complete = [True,True]

    def solve(self, data, part):
        
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
    solution().Answer()

#Answer to Part 1: 1936494
#Answer to Part 2: 1997106066