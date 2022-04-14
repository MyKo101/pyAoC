
import re
from math import sqrt,ceil

import sys
sys.path.insert(0,".")
from AoCDecorator import AoC

class probe:
    def __init__(self,vx,vy):
        self.v = [vx,vy]
        self.s = [0,0]
    
    def step(self):
        self.s[0] = self.s[0] + self.v[0]
        self.s[1] = self.s[1] + self.v[1]
        if self.v[0] < 1:
            self.v[0] = 0
        else:
            self.v[0] = self.v[0] - self.v[0]//abs(self.v[0])
        self.v[1] = self.v[1] - 1
    
    def hit(self,xmin,xmax,ymin,ymax):
        return xmin <= self.s[0] \
            and self.s[0] <= xmax \
            and ymin <= self.s[1] \
            and self.s[1] <= ymax
    
    def plummet(self,ymin):
        return self.v[1] < 0 and self.s[1] < ymin
    
    def launch(self,xmin,xmax,ymin,ymax):
        while True:
            #print(p)
            if self.hit(xmin,xmax,ymin,ymax):
                return 1
            if self.plummet(ymin):
                return 0
            else:
                self.step()

def count_probes(xmin,xmax,ymin,ymax):
    out = 0
    for i in range(ceil((-1 + sqrt(1+8*xmin))/2),xmax+1):
        for j in range(ymin,-ymin):
            p = probe(i,j)
            if p.launch(xmin,xmax,ymin,ymax):
                out +=1
    return out

@AoC(2021,17)
def solve(data,part):
    p = re.compile("target area: x=(-?\d*)..(-?\d*), y=(-?\d*)..(-?\d*)$")
    m = p.fullmatch(data[0])
    xmin,xmax,ymin,ymax = [
        int(m.group(i)) for i in range(1,5)
    ]

    if part == 1:
        return ymin*(ymin+1)//2
    if part == 2:
        return count_probes(xmin,xmax,ymin,ymax)


if(__name__ == "__main__"):
    solve()

# Answer 1: 12246
# Answer 2: 3528