
import sys
sys.path.insert(0,".")
from AoCDecorator import AoC


class point:
    def __init__(self,x,y):
        assert isinstance(x,int) and isinstance(y,int)
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"
    
    def __gt__(self,other):
        assert isinstance(other,fold)
        return getattr(self,other.axis) > other.num
    
    def __add__(self,other):
        assert isinstance(other,fold)
        if self > other:
            if other.axis == "x":
                return point(2*other.num - self.x,self.y)
            else:
                return point(self.x,2*other.num - self.y)
        return self
    
    def __eq__(self,other):
        assert isinstance(other,point)
        return self.x == other.x and self.y == other.y

class fold:
    def __init__(self,axis,num):
        assert axis in ["x","y"]
        assert isinstance(num,int)
        self.axis = axis
        self.num = num
    
    def __str__(self):
        return f"fold at {self.axis} = {self.num}"

class paper:
    def __init__(self,data):
        split_at = data.index("")

        self.folds = [
            fold(x[11],int(x[13:]))
            for x in data[split_at+1:]
        ]

        self.points = [
            point(int(a),int(b))
            for a,b in 
            [x.split(",") for x in data[:split_at]]
        ]
    
    def next_fold(self):
        if len(self.folds):
            c_fold = self.folds.pop(0)
            new_points = [p + c_fold for p in self.points]
            out_points = []
            for p in new_points:
                if p not in out_points:
                    out_points.append(p)
            self.points = out_points
        
    def do_folds(self,n=float("inf")):
        i = 0
        while i < n and len(self.folds):
            i +=1
            self.next_fold()
        return self.num_dots()

    def num_dots(self):
        return len(self.points)


    
    def __str__(self):

        h = max([p.y for p in self.points])+1
        w = max([p.x for p in self.points])+1
        out = [[" "]*w for _ in range(0,h)]
        for p in self.points:
            out[p.y][p.x] = "#"
        out = ["".join(x) for x in out]

        for i,iff in enumerate(self.folds):
            out[i] += f"  {iff}"
         
        out_str = "\n".join(out)
        return f"<Paper>\n{out_str}"


@AoC(2021,13)
def solve(data,part):
    X = paper(data)
    X.do_folds(1)
    if part == 1:
        return X.num_dots()
    if part == 2:
        X.do_folds()
        out = str(X).split("\n")[1:]
        out2 = ["#  " + x for x in out]

        return "\n" + "\n".join(out2)

if(__name__ == "__main__"):
    solve()

# Answer 1: 724
# Answer 2: 
#   ##  ###    ## ###  #### ###  #  # #
#  #  # #  #    # #  # #    #  # #  # #
#  #    #  #    # ###  ###  #  # #  # #
#  #    ###     # #  # #    ###  #  # #
#  #  # #    #  # #  # #    # #  #  # #
#   ##  #     ##  ###  #### #  #  ##  ####