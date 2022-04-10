
import sys
sys.path.insert(0,".")
from AoCDecorator import AoC

def h2b(x):
    d = {
         "0":"0000", "1":"0001", "2":"0010", "3":"0011",
         "4":"0100", "5":"0101", "6":"0110", "7":"0111",
         "8":"1000", "9":"1001", "A":"1010", "B":"1011",
         "C":"1100", "D":"1101", "E":"1110", "F":"1111",
        }
    return "".join([d[y] for y in x])

def b2d(x):
    return sum([2**i for i,y in enumerate(reversed(x)) if y == "1"])

def packet_literal(x):
    out = ""
    final = False
    while len(x) and not final:
        out += x[1:5]
        if x[0] == "0":
            final = True
        x = x[5:]
    return [b2d(out),x]

def packet_operator(x):
    len_type = x[0]
    if len_type == '0':
        out_len = b2d(x[1:16])
        x = x[16:]
        pk = x[:out_len]
        x = x[out_len:]
        response,y = packet(pk)
        content = [response]
        while len(y):
            response,y = packet(y)
            content += [response]
    else:
        out_num = b2d(x[1:12])
        x = x[12:]
        content = []
        for _ in range(0,out_num):
            response,x = packet(x)
            content += [response]
    return [content,x]

def packet(x):
    version = b2d(x[0:3])
    id = b2d(x[3:6])
    if id == 4:
        response,leftover = packet_literal(x[6:])
    else:
        response,leftover = packet_operator(x[6:])
    
    return [{"version":version,"id":id,"content":response},leftover]

def get_versions(x):
    if isinstance(x,int):
        return 0
    if isinstance(x,list):
        return sum([get_versions(y) for y in x])
    return x["version"] + get_versions(x["content"])

def decode(x):
    if isinstance(x,int):
        return [x]
    if isinstance(x,list):
        return [decode(y) for y in x]
    pk = decode(x["content"])
    match x["id"]:
        case 0:
            return sum(pk)
        case 1:
            out = 1
            for i in pk:
                out *= i
            return out
        case 2:
            return min(pk)
        case 3:
            return max(pk)
        case 4:
            return pk[0]
        case 5:
            return 1*(pk[0] > pk[1])
        case 6:
            return 1*(pk[0] < pk[1])
        case 7:
            return 1*(pk[0] == pk[1])
    
@AoC(2021,16)
def solve(data,part):
    bin_rep = h2b(data[0])
    pk,_ = packet(bin_rep)
    if part == 1:
        return get_versions(pk)
    if part == 2:
        return decode(pk)

if(__name__ == "__main__"):
    solve()

# Answer 1: 991
# Answer 2: 1264485568252