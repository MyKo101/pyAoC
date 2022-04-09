
import numpy as np

import sys
sys.path.insert(0,".")
from AoCDecorator import AoC

class board:
    def __init__(self,data):
        assert isinstance(data,np.ndarray)
        self.vals = data.astype(int)
        dims = self.vals.shape
        self.height = dims[0]-1
        self.width = dims[1]-1
        self.inf = np.sum(self.vals)+1
        self.d = np.array([[self.inf]*dims[1]]*dims[0])
        self.d[0,0] = 0
        self.visited = np.array([[False]*dims[1]]*dims[0])
        self.visited[0,0] = True
        self.pointlist = [(0,0)]
        self.end = (self.width,self.height)
    
    @staticmethod
    def raw(data):
        out = np.array([list(x) for x in data]).astype(int)
        return board(out)
        
    def insert_point(self,p):
        val_p = self.d[p]
        for i,cp in enumerate(self.pointlist):
            if val_p < self.d[cp]:
                self.pointlist.insert(i,p)
                return
        self.pointlist.append(p)
    
    def get_neighbours(self,p):
        out = []
        i = p[0]
        j = p[1]
        if i > 0:
            out += [(i-1,j)]
        if i < self.height:
            out += [(i+1,j)]
        if j > 0:
            out += [(i,j-1)]
        if j < self.width:
            out += [(i,j+1)]
        return out

    def get_vals(self,*args):
        out = []
        for ca in args:
            out += [self.vals[ca]]
        return out

    def check_visited(self,p):
        return self.visited[p]

    def expand(self,n):
        base = self.vals.copy()
        htup = tuple((1 + ((base + i - 1) % 9) for i in range(0,n)))
        out_h = np.hstack(htup)
        vtup = tuple((1 + ((out_h + i - 1) % 9) for i in range(0,n)))
        out = np.vstack(vtup)
        return board(out)
            
    def next(self):
        current_point = self.pointlist.pop(0)
        current_d = self.d[current_point]
        neighbours_all = self.get_neighbours(current_point)
        neighbours = [x for x in neighbours_all if not self.check_visited(x)]
        neighbour_vals = self.get_vals(*neighbours)
        neighbour_d = [x + current_d for x in neighbour_vals]
        for i,cn in enumerate(neighbours):
            self.d[cn] = neighbour_d[i]
            self.insert_point(cn)
            self.visited[cn] = True
    
    def done(self):
        return self.visited[self.end]
    
    def do(self):
        while not self.done():
            self.next()
        return self.d[self.end]

@AoC(2021,15)
def solve(data,part):
    X = board.raw(data)
    if part == 1:
        return X.do()
    if part == 2:
        Y = X.expand(5)
        return Y.do()

if(__name__ == "__main__"):
    solve()

# Answer 1: 652
# Answer 2: 2938