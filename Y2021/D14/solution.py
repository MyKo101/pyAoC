
from collections import defaultdict

import sys
sys.path.insert(0,".")
from AoCDecorator import AoC

class polymer:
    def __init__(self,data):
        template = data[0]
        self.template = defaultdict(lambda:0)
        for i,_ in enumerate(template[1:]):
            self.template[template[i:i+2]] += 1
        
        self.mappings = defaultdict(lambda:"")
        for x in data[2:]:
            self.mappings[x[0:2]] = [x[0]+x[6],x[6]+x[1]]
        
        self.lastvalue = data[0][-1]

    def do_next(self):
        template = self.template.copy()
        mappings = self.mappings.copy()
        out = defaultdict(lambda:0)
        for ik in template:
            v = template[ik]
            if ik in mappings:
                mp = mappings[ik]
                for cp in mp:
                    out[cp] += v
            else:
                out[ik] = v
        self.template = out
            
    def do_for(self,n):
        for i in range(0,n):
            #print(f"Running {i=}")
            self.do_next()

    def score(self):
        tally = defaultdict(lambda:0)
        tally[self.lastvalue] = 1
        for x in self.template:
            v = self.template[x]
            tally[x[0]] += v
            #tally[x[1]] += v
        v = tally.values()
        return max(v) - min(v)

    def __str__(self):
        out = "<polymer>\n "
        for ct in self.template:
            out += f"[{ct} = {self.template[ct]}]   "
        out += "\n<mapping>\n "
        for ci in self.mappings:
            out += f"['{ci}' -> {self.mappings[ci]}]   "
        return out
    

@AoC(2021,14)
def solve(data,part):
        
    X = polymer(data)
    X.do_for(10)
    if part == 2:
        X.do_for(30)
    return X.score()

if(__name__ == "__main__"):
    solve()

# Answer 1: 3906
# Answer 2: 4441317262452