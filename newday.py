
import sys
import os
import requests

def getdir(year,day,*args):
    return os.path.join(os.getcwd(),f"Y{year}",f"D{day:02}",*args)

def pytemplate(year,day):

    out = [
        "",
        "import sys",
        "sys.path.insert(0,'.')",
        "from AoCClass import AoC",
        "",
        "class solution(AoC):",
        f"    year = {year}",
        f"    day = {day}",
        "    example = []",
        "    complete = [False,False]",
        "",
        "    def solve(self, data, part):",
        "        pass",
        "",
        "",
        "if(__name__ == '__main__'):",
        "    solution().Answer()"
        ]

    return "\n".join(out)

def main():
    year = int(sys.argv[1])
    day = int(sys.argv[2])

    dir_name = getdir(year,day)
    pyfile_name = getdir(year,day,"solution.py")
    data_name = getdir(year,day,"data")
    pyfile_open = f"code {pyfile_name} -r"
    data_open = f"code {data_name} -r"
    data_browser = f"start https://adventofcode.com/{year}/day/{day}/input"

    if os.path.isdir(dir_name):
        print("Directory Already Exists!")
        return None

    os.makedirs(dir_name)

    with open(pyfile_name,"w") as f:
        f.write(pytemplate(year,day))

    open(data_name,"w").close()

    os.system(pyfile_open)
    os.system(data_open)
    os.system(data_browser)

    
    print("Please make sure you insert data into data file")



if(__name__ == "__main__"):
    main()



