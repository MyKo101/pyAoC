import os
import re


def md_template(tbl):
    template_file = os.path.join(os.getcwd(),"templates","readme")
    with open(template_file,"r") as f:
        template = f.read()
    return template.format(tbl=tbl)

def main():
    daypattern = re.compile("^.\\\\Y[0-9]{4}\\\\D[0-9]{2}$")
    prgpattern = re.compile("(?<=#' Part [12]: )(.*)")


    daypaths = [path for path,_,_ in 
                    os.walk(".") 
                        if bool(daypattern.search(path))]
    
    tbl = "| Year | Day | Part 1 | Part 2 |"
    tbl += "\n|-|-|-|-|"
    for c_day in daypaths:
        c_sol = c_day + "\\solution.py"
        prglines = [prgpattern.findall(line)[0] for line in open(c_sol) if prgpattern.search(line)]
        year = int(re.findall("(?<=^\.\\\\Y)([0-9]{4})",c_day)[0])
        day = int(re.findall("(?<=\\\\D)([0-9]{2})",c_day)[0])

        if prglines[0] == "Done":
            p1 = ":heavy_check_mark:"
        else:
            print(f"Year {year} Day {day} started, Part 1 Not Done")

        if prglines[1] == "Done":
            p2 = ":heavy_check_mark:"
        else:
            print(f"Year {year} Day {day} started, Part 2 Not Done")

        tbl += f"\n|{year}|{day}|{p1}|{p2}|"

    out_text = md_template(tbl)
    with open("README.md","w") as f:
        f.write(out_text)

if(__name__ == "__main__"):
    main()