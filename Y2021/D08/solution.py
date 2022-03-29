
import sys
sys.path.insert(0,".")
from AoCDecorator import AoC

def get_words(x):
    return ["".join(sorted(y)) for y in x.split() if y != "|"]

def unique(x):
    assert isinstance(x,list)
    z = x
    x.sort()
    return list(set(z))

def get_by_length(x,l):
    return [y for y in x if len(y) == l]

def get_by_subset(x,s):
    found = [all([(s0 in y) for s0 in s]) for y in x]
    return [i for i,v in zip(x,found) if v]

def get_by_length_subset(x,l,s):
    out = get_by_length(x,l)
    return get_by_subset(out,s)

def get_intersect(a,b):
    inter = list(set(a).intersection(set(b)))
    inter.sort()
    return ["".join(inter)]

class display:
    def __init__(self,x):
        assert isinstance(x,str)
        lhs,rhs = x.split(" | ") 
        self.rhs = get_words(rhs)
        self.tbd = unique(get_words(lhs) + self.rhs)
        self.lens = [len(y) for y in self.tbd]
        self.mapping = [None]*10

        while not self.done():
            for i in range(0,10):
                self.find(i)
        
               
    def result(self,part):
        assert self.done()
        if part == 1:
            out = [self.output(x) in [1,4,7,8] for x in self.rhs]
            return sum(out)
        if part == 2:
            out = [str(self.output(x)) for x in self.rhs]
            return int("".join(out))
    
    def output(self,x):
        assert self.done()
        return [i for i,y in enumerate(self.mapping) if x == y][0]

    def done(self):
        return not len(self.tbd)
    
    def are_done(self,*args):
        return all([self.mapping[x] is not None for x in args])

    def find(self,val):
        if self.mapping[val] is not None:
            return None

        out = self.find2(val)
        if out is not None:
            self.tbd = [x for x in self.tbd if x != out]
        self.mapping[val] = out

    def find2(self,val):

        if val == 1:
            return get_by_length(self.tbd,2)[0]
        if val == 4:
            return get_by_length(self.tbd,4)[0]
        if val == 7:
            return get_by_length(self.tbd,3)[0]
        if val == 8:
            return get_by_length(self.tbd,7)[0]

        if val == 9:
            if self.are_done(0,6):
                return get_by_length(self.tbd,6)[0]
            if self.are_done(4):
                return get_by_length_subset(self.tbd,6,self.mapping[4])[0]
                    
        if val == 0:
            if self.are_done(6,9):
                return get_by_length(self.tbd,6)[0]
            if self.are_done(1,9):
                return get_by_length_subset(self.tbd,6,self.mapping[1])[0]
            
        if val == 6:
            if self.are_done(0,9):
                return get_by_length(self.tbd,6)[0]

        if val == 2:
            if self.are_done(3,5):
                return get_by_length(self.tbd,5)[0]
            

        if val == 3:
            if self.are_done(2,5):
                return get_by_length(self.tbd,5)[0]
            if self.are_done(1):
                return get_by_length_subset(self.tbd,5,self.mapping[1])[0]


        if val == 5:
            if self.are_done(2,3):
                return get_by_length(self.tbd,5)[0]
            if self.are_done(6,9):
                return get_intersect(self.mapping[6],self.mapping[9])[0]



@AoC(2021,8)
def solve(data,part):
    return sum([display(x).result(part) for x in data])

if(__name__ == "__main__"):
    solve()

# Answer 1: 310
# Answer 2: 915941