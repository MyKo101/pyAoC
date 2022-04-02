
import numpy as np

import sys
sys.path.insert(0,".")
from AoCDecorator import AoC


class board:
    __slots__ = ["b","f","w","h","s"]

    def __init__(self,data):
        self.b = np.matrix([list(x) for x in data]).astype("int")
        dims = self.b.shape
        self.h = dims[0] # nrows => i & h
        self.w = dims[1] # ncols => j & w
        self.f = np.matrix([[False]*self.w]*self.h)
        self.s = 0
    
    def reset_flash(self):
        self.f[:,:] = False
    
    def check_loc(self,i,j):
        return 0 <= i and i < self.h \
            and 0 <= j and j < self.w

    def check_full(self):
        return self.b.sum() == 0
            
    def neighbour_coords(self,i,j):
        poss = [
            [i-1,j-1],[i-1,j],[i-1,j+1],
            [i  ,j-1]        ,[i  ,j+1],
            [i+1,j-1],[i+1,j],[i+1,j+1],
        ]
        return [[i2,j2] for i2,j2 in poss if self.check_loc(i2,j2)]
        
    def get_flashes(self):
        flashed_M = np.logical_and(self.b > 9,np.logical_not(self.f))
        return list(zip(*np.where(flashed_M)))

    def has_high(self):
        return (self.b > 9).any()

    def step(self):
        self.b +=1
        while self.has_high():
            [self.flash(i,j) for i,j in self.get_flashes()]  
        self.inc_score()
        self.reset_flash()
    
    def flash(self,i,j):
        self.b[i,j] = 0
        self.f[i,j] = True
        nb = self.neighbour_coords(i,j)
        for i,j in nb:
            if not self.f[i,j]:
                self.b[i,j] += 1
    
    def run1(self,n):
        for _ in range(0,n):
            self.step()
        return self.s

    def run2(self):
        i = 0
        while not self.check_full():
            i += 1
            self.step()
        return i
        
    def inc_score(self):
        self.s += self.f.sum()
        
    def __str__(self):
        out = "<Board>\n"
        for i in range(0,self.h):
            for j in range(0,self.w):
                bv = self.b[i,j]
                if bv > 0:
                    out += f" {self.b[i,j]:2}"
                else:
                    out += f" \033[91m{self.b[i,j]:2}\033[0m"
            out +="\n"
        return out

@AoC(2021,11)
def solve(data,part):
    brd = board(data)
    if part == 1:
        return brd.run1(100)
    if part == 2:
        return brd.run2()

if(__name__ == "__main__"):
    solve()

# Answer 1: 1601
# Answer 2: 368