import os
import importlib


def md_template(tbl):
    return(
"""
## Advent of Code

This is my work through the historic Advent of Code
activities, tracking my progress here and including
the python code used to solve the problems.

In order to complete the Advent of Code, I have created
an AoC Class and each solution is a subclass with
certain attributes provided.

My own data (supplied by Advent of Code) is included in
each directory and each file can be run (provided that the
AoCClass.py file is in the project root)

## Progress
"""
    f"{tbl}"
    )

def getdir_prefix(path,pre):
    return [cd for cd in os.listdir(path) if cd[0] == pre]

def year_progress(year_dir):
    D_dirs = getdir_prefix(year_dir,"D")

    out = []

    for d in D_dirs:
        c_modname = year_dir + "." + d + ".solution"
        c_mod = importlib.import_module(c_modname)
        c_sol = c_mod.solution()
        c_done = c_sol.complete
        out.append({
            "Year":int(year_dir[1:]),
            "Day":int(d[1:]),
            "Part1":c_done[0],
            "Part2":c_done[1]
        })

    return out

def print_progress_line(prg):
    p1 = ":heavy_check_mark:" if prg['Part1'] else ""
    p2 = ":heavy_check_mark:" if prg['Part2'] else ""
    return f"|{prg['Year']}|{prg['Day']}|{p1}|{p2}|"

def print_progress(prg):
    prg_lines = [print_progress_line(x) for x in prg]
    return "\n".join(["|Year|Day|Part 1|Part 2|"] +["|-|-|-|-|"] + prg_lines)


alldirs = os.listdir(".")
Y_dirs = getdir_prefix(".","Y")
prg = []
for y in Y_dirs:
    prg += year_progress(y)

tbl = print_progress(prg)

out_txt = md_template(tbl)

with open("README.md","w") as f:
    f.write(out_txt)