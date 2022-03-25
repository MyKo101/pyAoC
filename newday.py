
import sys
import os


def getdir(year,day,*args):
    return os.path.join(os.getcwd(),f"Y{year}",f"D{day:02}",*args)

def pytemplate(year,day):
    template_file = os.path.join(os.getcwd(),"templates","dayfile")
    with open(template_file,"r") as f:
        template = f.read()

    return template.format(year=year,day=day)

def main():
    year = int(sys.argv[1])
    day = int(sys.argv[2])

    dir_name = getdir(year,day)

    if os.path.isdir(dir_name):
        print("Directory Already Exists!")
        return None

    pyfile_name = getdir(year,day,"solution.py")
    data_name = getdir(year,day,"data")
    pyfile_open = f"code {pyfile_name} -r"
    data_open = f"code {data_name} -r"
    data_browser = f"start https://adventofcode.com/{year}/day/{day}/input"

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



