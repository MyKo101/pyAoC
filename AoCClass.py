
import os

class AoC:
    example = []
    year = 0
    day = 0
    complete = [False,False]

    def __init__(self):
        pass

    def __str__(self):
        return f"An AoC solution for Year {self.year} and Day {self.day}"

    def solve(self,data,part):
        pass

    def Answer(self,type="data"):
        if(not self.complete[0] and not self.complete[1]):
            print("No solutions found")
            return 0
        
        if type == "example":
            print("Solving for example...")
            data_in = self.Example()
        elif type == "data":
            print("Solving...")
            data_in = self.Data()
        else:
            return "'type' must be either 'example' or 'data' (or missing)"

        if self.complete[0]:
            ans1 = self.solve(data_in,1)
            print(f"Answer to Part 1: {ans1}") 
        if self.complete[1]:
            ans2 = self.solve(data_in,2)
            print(f"Answer to Part 2: {ans2}")
        
        return 1

    def Example(self):
        return self.example

    def Data(self):
        with open(self.dir("data"),"r") as f:
            return f.read().split("\n")

    def dir(self,*args):
        return os.path.join(f"Y{self.year}",f"D{self.day:02}",*args)
