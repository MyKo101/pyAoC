
import sys
import os
import re


def getdir(year,day,*args):
    return os.path.join(os.getcwd(),f"Y{year}",f"D{day:02}",*args)

def pytemplate(year,day):
    template_file = os.path.join(os.getcwd(),"templates","dayfile")
    with open(template_file,"r") as f:
        template = f.read()

    return template.format(year=year,day=day)

def newday(year,day):
    dir_name = getdir(year,day)

    if os.path.isdir(dir_name):
        print("Directory Already Exists!")
        return None

    pyfile_name = getdir(year,day,"solution.py")
    data_name = getdir(year,day,"data")
    pyfile_open = f"code {pyfile_name} -r"
    data_open = f"code {data_name} -r"
    data_browser = f"start https://adventofcode.com/{year}/day/{day}/input"
    question_browser = f"start https://adventofcode.com/{year}/day/{day}"

    os.makedirs(dir_name)

    with open(pyfile_name,"w") as f:
        f.write(pytemplate(year,day))

    open(data_name,"w").close()

    os.system(pyfile_open)
    os.system(data_open)
    os.system(question_browser)
    os.system(data_browser)

    
    print("Please make sure you insert data into data file")

def nextday(year):
    daypattern = re.compile(f"(?<=^.\\\\Y{year}\\\\D)([0-9]{{2}})$")

    daysdone = [int(daypattern.findall(path)[0]) 
                    for path,_,_ in os.walk(".") 
                        if bool(daypattern.search(path))]
    
    next = max(daysdone)+1 if len(daysdone) else 1
   
    newday(year,next)
    

def main():
    if len(sys.argv) == 2:
        nextday(int(sys.argv[1]))
    elif len(sys.argv) == 3:
        newday(int(sys.argv[1]),int(sys.argv[2]))
    else:
        print("Incorrect Number of Arguments")


if(__name__ == "__main__"):
    main()



