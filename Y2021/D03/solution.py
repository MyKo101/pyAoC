
#' Part 1: Done
#' Part 2: Done

import numpy as np

import sys
sys.path.insert(0,'.')
from AoCDecorator import AoC

def get_one_common(X):
    return sum(X) >= len(X)/2

def get_gamma(X):
    return (1*get_one_common(X))

def toBin(x):
    pow2 = [2**j for j in range(len(x)-1,-1,-1)]
    return sum(x*pow2)

def get_oxygen(X):
    def criteria_oxy(V):
        mc = 1*get_one_common(V)
        return [i for i,x in enumerate(V) if x==mc]
    
    return get_filter(X,criteria_oxy)

def get_c02(X):
    def criteria_c02(V):
        mc = 1*get_one_common(V)
        return [i for i,x in enumerate(V) if x!=mc]
    
    return get_filter(X,criteria_c02)

def get_filter(X,criteria):
    i = 0
    M = len(X.T)
    while len(X) > 1 and i < M:
        bit_condition = criteria(X[:,i])
        X = X[bit_condition,:]
        i += 1
    return X[0,:]

@AoC(2021,3)
def solve(data,part):
    dl = [list(x) for x in data]

    dm = np.array(dl).astype(int)

    if part == 1:
        gamma = get_gamma(dm)

        beta = toBin(1-gamma)
        gamma2 = toBin(gamma)
        return beta*gamma2

    if part == 2:
        oxy = toBin(get_oxygen(dm))
        c02 = toBin(get_c02(dm))

        return oxy*c02


if(__name__ == '__main__'):
    solve()