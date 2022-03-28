
import sys
sys.path.insert(0,".")
from AoCDecorator import AoC

def align_to(data,v,d):
    return sum([d(x-v) for x in data])

@AoC(2021,7)
def solve(data,part):
    
    if part == 1:
        d = lambda a: abs(a)
    if part == 2:
        d = lambda a: abs(a)*(abs(a)+1)//2

    data2 = [int(x) for x in data[0].split(",")]

    x1 = min(data2)
    x2 = max(data2)
    dl = [align_to(data2,i,d) for i in range(x1,x2+1)]
    return min(dl)


if(__name__ == "__main__"):
    solve()

# Answer 1: 329389
# Answer 2: 86397080