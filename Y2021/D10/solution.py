
import sys
sys.path.insert(0,".")
from AoCDecorator import AoC


ob= ["(","[","{","<"]
cb = [")","]","}",">"]
osc1 = [3,57,1197,25137]
osc2 = [1,2,3,4]

def get_ref(x,input,output):
    return [output[i] for i,y in enumerate(input) if x == y][0]


def get_close(open):
    assert open in ob, "Input must be open bracket"
    return get_ref(open,ob,cb)

def get_score1(close):
    assert close in cb, "Input must be closed bracket"
    return get_ref(close,cb,osc1)

def get_score2(stack):
    scores = [get_ref(x,ob,osc2) for x in stack]
    out = 0
    for sc in scores:
        out = 5*out + sc
    return out



def check_val(x,close):
    return x in ob + [close]

def step(text,stack):
    x = text[0]
    if x in ob:
        return [text[1:],[x] + stack]
    elif x == get_close(stack[0]):
        return [text[1:],stack[1:]]
    else:
        return ["ERROR",x]

def eval_row(text):
    stack = []
    while len(text) and text != "ERROR":
        text,stack = step(text,stack)

    if text == "ERROR":
        return [get_score1(stack),"Corrupt"]
    if len(stack):
        return [get_score2(stack),"Incomplete"]
    return None


@AoC(2021,10)
def solve(data,part):
    out = [eval_row(x) for x in data]
    if part == 1:
        return sum([x[0] for x in out if x[1] == "Corrupt"])
    if part == 2:
        out2 = [x[0] for x in out if x[1] == "Incomplete"]
        out2.sort()
        return out2[len(out2)//2]

if(__name__ == "__main__"):
    solve()

# Answer 1: 362271
# Answer 2: 1698395182