
import numpy as np

import sys
sys.path.insert(0,'.')
from AoCClass import AoC

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


class solution(AoC):
    year = 2021
    day = 3
    example = ['00100', '11110', '10110', '10111', '10101', '01111',
            '00111', '11100', '10000', '11001', '00010', '01010']
    complete = [True,True]

    def solve(self, data, part):
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
    solution().Answer()