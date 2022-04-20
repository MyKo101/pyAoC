
import re
from itertools import product

import sys
sys.path.insert(0,".")
from AoCDecorator import AoC

class sn:
    pair_pattern = re.compile("(\[\d+,\d+\])")
    split_pattern = re.compile("(\d{2,})")
    num_pattern = re.compile("(\d+)")
    pair_left_pattern = re.compile("\[(\d+),")
    pair_right_pattern = re.compile(",(\d+)\]")

    def __init__(self,input):
        assert type(input) is str
        self.txt = input
        self.reduce()
    
    def __str__(self):
        return f"{self.txt}"
    
    def __repr__(self):
        return f"sn('{str(self)}')"
    
    def depth(self,pos):
        return self.txt[0:pos+1].count("[") - self.txt[0:pos].count("]")
    
    def get(self,pos):
        return self.txt[pos[0]:pos[1]]
    
    def find_explode(self):
        match = sn.pair_pattern.search(self.txt)
        while match is not None and self.depth(match.span()[0]) <= 4:
            match = sn.pair_pattern.search(self.txt,match.span()[0]+1)
        if match is not None:
            return match.span()
    
    def find_split(self):
        match = sn.split_pattern.search(self.txt)
        if match is not None:
            return match.span()
    
    def replace(self,pos,new):
        pre = self.txt[:min(pos)]
        post = self.txt[max(pos):]
        self.txt = f"{pre}{new}{post}"
    
    def next_num(self,pos):
        match = sn.num_pattern.search(self.txt,max(pos)+1)
        if match is not None:
            return match.span()
    
    def prev_num(self,pos):
        match = sn.num_pattern.search(self.txt,0,min(pos))
        if match is not None:
            match2 = sn.num_pattern.search(self.txt,match.span()[1]+1,min(pos))
            while match2 is not None:
                match = match2
                match2 = sn.num_pattern.search(self.txt,match.span()[1]+1,min(pos))
            return match.span()
    
    def explode(self,pos):
        exp_val = self.get(pos)
        self.replace(pos,0)
        pos = (pos[0],pos[0]+1)

        prev_pos = self.prev_num(pos)
        if prev_pos is not None:
            p_num = self.get(prev_pos)
            exp_l = sn.pair_left_pattern.findall(exp_val)[0]
            new_val = str(int(p_num) + int(exp_l))
            self.replace(prev_pos,new_val)
            change = len(new_val) - len(p_num)
            pos = tuple(x + change for x in pos)

        next_pos = self.next_num(pos)
        if next_pos is not None:
            n_num = int(self.get(next_pos))
            exp_r = int(sn.pair_right_pattern.findall(exp_val)[0])
            self.replace(next_pos,n_num + exp_r)
    
    def split(self,pos):
        s_val = int(self.get(pos))
        lhs = s_val//2
        rhs = s_val - lhs
        new_val = f"[{lhs},{rhs}]"
        self.replace(pos,new_val)
    
    def reduce_step(self):
        exp_pos = self.find_explode()
        if exp_pos is not None:
            self.explode(exp_pos)
            return True
        split_pos = self.find_split()
        if split_pos is not None:
            self.split(split_pos)
            return True
        return False
    
    def reduce(self):
        while self.reduce_step():
            pass
    
    def __add__(self,other):
        assert type(other) is sn
        return sn(f"[{self},{other}]")
    
    def score(self):
        cache = self.txt
        pair = sn.pair_pattern.search(self.txt)
        while pair is not None:
            pair_pos = pair.span()
            pair_val = self.get(pair_pos)
            pair_left = int(sn.pair_left_pattern.findall(pair_val)[0])
            pair_right = int(sn.pair_right_pattern.findall(pair_val)[0])
            new_val = 3*pair_left + 2*pair_right
            self.replace(pair_pos,new_val)
            pair = sn.pair_pattern.search(self.txt)
        out = int(self.txt)
        self.txt = cache
        return out


@AoC(2021,18)
def solve(data,part):
    if part == 1:
        out = sn(data[0])

        for x in data[1:]:
            out += sn(x)

        return out.score()
    if part == 2:
        all_rows = range(len(data))
        out = 0
        for i,j in product(all_rows,all_rows):
            if i == j:
                continue
            
            csn = sn(data[i]) + sn(data[j])
            out = max(out,csn.score())
        return out


if(__name__ == "__main__"):
    solve()
    
# Answer 1: 4289
# Answer 2: 4807
