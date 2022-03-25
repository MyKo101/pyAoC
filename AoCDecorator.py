import os

def datapath(year,day):
    return os.path.join(f"Y{year}",f"D{day:02}","data")

def AoC(year,day):
    def inner(fun):
        data_file = datapath(year,day)
        #data_file = os.path.join(f"Y{year}",f"D{day:02}","data")
        def wrapper():
            print("Solving...")
            with open(data_file,"r") as f:
                data_in = f.read().split("\n")
            ans1 = fun(data_in,1)
            print(f"# Answer 1: {ans1}")
            ans2 = fun(data_in,2)
            print(f"# Answer 2: {ans2}")
            return [ans1,ans2]
        
        return wrapper
    return inner