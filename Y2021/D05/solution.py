
import numpy as np
import re

import sys
sys.path.insert(0,".")
from AoCDecorator import AoC

class point:
    def __init__(self,x,y):
        self.x = int(x)
        self.y = int(y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return str(self)

class line:
    def __init__(self,p1,p2):
        assert isinstance(p1,point) and isinstance(p2,point)
        self.p1 = p1
        self.p2 = p2
    
    def ishorizontal(self):
        return self.p1.y == self.p2.y
    
    def isvertical(self):
        return self.p1.x == self.p2.x
    
    def isdiagonal(self):
        dx = self.p1.x - self.p2.x
        dy = self.p1.y - self.p2.y
        return dx != 0 and dy != 0 and abs(dx) == abs(dy)

    def points(self,part):

        x = [self.p1.x,self.p2.x]
        y = [self.p1.y,self.p2.y]
        dx = range2(x[0],x[1])
        dy = range2(y[0],y[1])

        if len(dx) == 1 and len(dy) == 1:
            return [point(x[0],y[0])]
        if len(dx) == 1:
            return [point(x[0],j) for j in dy]
        if len(dy) == 1:
            return [point(i,y[0]) for i in dx]
        if part == 2 and len(dx) == len(dy):
            return [point(i,j) for i,j in zip(dx,dy)]
        
    def __str__(self):
        return f"{self.p1} -> {self.p2}"

    def __repr__(self):
        return f"\n<line object>: {self}"

class floor:
    def __init__(self,h,w):
        self.map = np.array([[0]*(h)]*(w))

    def __str__(self):
        return str(self.map.T)
    
    def __repr__(self):
        return str(self)

    def addpoint(self,x):
        assert isinstance(x,point)
        self.map[x.x,x.y] +=1
    
    def addline(self,x,part):
        assert isinstance(x,line)
        pl = x.points(part)
        if pl is not None:
            for y in pl:
                self.addpoint(y)
    
    def score(self):
        return sum(sum(self.map > 1))
        
def makeline(X):
    X2 = re.findall("([0-9]*),([0-9]*) -> ([0-9]*),([0-9]*)",X)[0]
    return line(point(X2[0],X2[1]),point(X2[2],X2[3]))

def size(lst):
    maxx = max(max([[l.p1.x,l.p2.x] for l in lst]))+1
    maxy = max(max([[l.p1.y,l.p2.y] for l in lst]))+1
    return [maxx,maxy]
 
def range2(a,b):
    assert isinstance(a,int) and isinstance(b,int)
    if a < b:
        return range(a,b+1)
    if b < a:
        return range(a,b-1,-1)
    if a == b:
        return range(a,b+1)

@AoC(2021,5)
def solve(data,part):
    lst = [makeline(x) for x in data]
    sz = size(lst)
    M = floor(sz[0]+1,sz[1]+1)
    for l in lst:
        M.addline(l,part)
    return M.score()

if(__name__ == "__main__"):
    solve()

# Answer 1: 6666
# Answer 2: 19081