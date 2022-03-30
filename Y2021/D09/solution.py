
import numpy as np

import sys
sys.path.insert(0,".")
from AoCDecorator import AoC

class heatmap:
    def __init__(self,data):
        self.map = np.array([[int(y) for y in x] for x in data])
        self.basinmap = heatmap.blank_basin(self.width(),self.height())

        self.basinNA = self.basinmap.max()+10
        self.calc_basins()

    def height(self):
        return self.map.shape[0]

    def width(self):
        return self.map.shape[1]
        
    def depth(self,i,j):
        if self.check_loc(i,j):
            return self.map[i,j]
    
    def basin(self,i,j):
        if self.check_loc(i,j):
            return self.basinmap[i,j]
    
    @staticmethod
    def blank_basin(w,h):
        out = [list(range(1+i*w,1+(i+1)*w)) for i in range(0,h)]
        return np.array(out)
        
    def check_loc(self,i,j):
        return 0 <= i and i < self.height() \
            and 0 <= j and j < self.width()

    def get_region(self,i,j):
        coords = [[i,j],[i-1,j],[i+1,j],[i,j-1],[i,j+1]]
        return [[i,j] for i,j in coords if self.depth(i,j) is not None]

    def get_depths(self,lst):
        return [self.depth(i,j) for i,j in lst]
    
    def get_basins(self,lst):
        return [self.basin(i,j) for i,j in lst]
    
    def set_basin(self,i,j,val):
        self.basinmap[i,j] = val
    
    def check_basin(self,i,j):
        assert self.check_loc(i,j), "value out of bounds"
        if self.depth(i,j) == 9:
            self.set_basin(i,j,self.basinNA)
            return None

        region = self.get_region(i,j)
        depths = self.get_depths(region)
        basins = self.get_basins(region)
        
        lowest = depths.index(min(depths))
        lowest_b = basins[lowest]
        self.set_basin(i,j,lowest_b)
    
    def calc_basins(self):
        Y = 0
        while (self.basinmap != Y).any():
            Y = self.basinmap.copy()
            for i in range(0,self.height()):
                for j in range(0,self.width()):
                    self.check_basin(i,j)
                
        basinvals = np.unique(self.basinmap)
        basinvals = basinvals[basinvals != self.basinNA]
        self.basinVals = basinvals
    
    def get_basin_fun(self,b,fun):
        assert b in self.basinVals
        return fun(self.map[self.basinmap == b])

    def get_basins_fun(self,fun):
        return [self.get_basin_fun(b,fun) for b in self.basinVals]
    
    def get_score(self,part):
        if part == 1:
            scores = self.get_basins_fun(min)
            return sum([x+1 for x in scores])
        if part == 2:
            scores = self.get_basins_fun(len)
            scores.sort(reverse=True)
            return np.prod(scores[0:3])
            
@AoC(2021,9)
def solve(data,part):
    return heatmap(data).get_score(part)

if(__name__ == "__main__"):
    solve()
    
# Answer 1: 465
# Answer 2: 1269555