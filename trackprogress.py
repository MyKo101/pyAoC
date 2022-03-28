import os
import re
import pandas as pd


def md_template(tbl):
    template_file = os.path.join(os.getcwd(),"templates","readme")
    with open(template_file,"r") as f:
        template = f.read()
    return template.format(tbl=tbl)


def get_progress(year,day,pt):
    sol_file = f"Y{year}\\D{day:02}\\solution.py"
    prglines = [pt.findall(line)[0] for line in open(sol_file) if pt.search(line)]
    prg_bool = ['1' in prglines,'2' in prglines]
    return " ".join(["[x]" if x else "[ ]" for x in prg_bool])
     

def get_paths(pt):
    return [path for path,_,_ in os.walk(".") if bool(pt.search(path))]

def pull_pattern(x,pt,conv=None):
    if conv is None:
        return [pt.findall(y)[0] for y in x]        
    return [conv(pt.findall(y)[0]) for y in x]

def progress_table():
    
    filepattern = re.compile("^.\\\\Y[0-9]{4}\\\\D[0-9]{2}$")
    yearpattern = re.compile("(?<=\\\\Y)([0-9]{4})")
    daypattern = re.compile("(?<=\\\\D)([0-9]{2})")
    prgpattern = re.compile("(?<=# Answer )([12])")

    daypaths = get_paths(filepattern)

    years = pull_pattern(daypaths,yearpattern,int)
    days = pull_pattern(daypaths,daypattern,int)
    parts = [get_progress(i,j,prgpattern) for i,j in zip(years,days)]

    prg_df = pd.DataFrame(data={
        "year":years,
        "day":days,
        "part":parts
    })

    prg_df_pivot = prg_df \
        .pivot_table(index="day",columns="year",values="part", \
            fill_value="",aggfunc=lambda x: x)

    return prg_df_pivot.to_markdown(tablefmt="github")

def main():
    out_text = md_template(tbl = progress_table())
    with open("README.md","w") as f:
        f.write(out_text)

if(__name__ == "__main__"):
    main()