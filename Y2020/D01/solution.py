
#' Part 1: Done
#' Part 2: Done

import numpy as np

import sys
sys.path.insert(0,'.')
from AoCDecorator import AoC

class index:

    def __init__(self,num,max):
        self.val = list(range(0,num))
        self.max = max
        self.endval = list(range(max-num,max))

    def of(self,data):
        return [data[j] for j in self.val]

    def next(self):
        assert not self.done(), "Index Vector is done"
        self.val[-1] += 1
        for j in range(1,len(self.val)):
            if self.val[-j] == self.max-j+1:
                self.val[-j-1] += 1
                self.val[-j:] = list(range(self.val[-j-1]+1,self.val[-j-1]+j+1))
        return self
        
    def done(self):
        return self.val == self.endval

@AoC(2020,1)
def solve(data,part):
    data2 = [int(x) for x in data]

    target = 2020

    if part == 1:
        i = index(2,len(data2))
    if part == 2:
        i = index(3,len(data2))

    while not i.done() and sum(i.of(data2)) != target:
        i.next()
    
    return np.prod(i.of(data2))

if(__name__ == '__main__'):
    solve()

# Answer to Part 1: 381699
# Answer to Part 2: 111605670