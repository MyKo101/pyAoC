
from collections import defaultdict, Counter

import sys
sys.path.insert(0,".")
from AoCDecorator import AoC

class graph:
    def __init__(self,data):
        self.graph = defaultdict(set)
        for x in data:
            self.add(*x.split("-"))
        
    def add(self,node1,node2):
        self.graph[node1].add(node2)
        self.graph[node2].add(node1)

    def getpaths(self,part):
        openpaths = [["start",x] for x in self.graph["start"] if x != "end"]
        donepaths = [x for x in openpaths if x[-1]=="end"]

        if len(donepaths):
            openpaths = [x for x in openpaths if x != ["start","end"]]

        while len(openpaths):
            self.getpaths_next(openpaths,donepaths,part)
        
        return donepaths
        
    def getpaths_next(self,openpaths,donepaths,part):
        current_path = openpaths.pop()
        current_node = current_path[-1]

        new_paths = [current_path + [x] for x in self.graph[current_node] \
                        if graph.pathcheck(x,current_path,part)]
        
        for np in new_paths:
            if np[-1] == "end":
                donepaths +=  [np]
            else:
                openpaths += [np]
            
    @staticmethod
    def pathcheck(node,path,part):
        assert isinstance(node,str)
        if node == "start":
            return False
        if node.isupper() or node not in path:
            return True
        if part == 1:
            return False
        if part == 2:
            if path.count(node) > 1:
                return False
            cpath = Counter(path + [node])
            out = sum([cpath[x]>1 for x in cpath if x != "start" and x.islower()])
            return out < 2
    


@AoC(2021,12)
def solve(data,part):
    X = graph(data)
    return len(X.getpaths(part))

if(__name__ == "__main__"):
    solve()

# Answer 1: 4749
# Answer 2: 123054