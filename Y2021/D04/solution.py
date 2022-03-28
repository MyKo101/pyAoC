
import numpy as np

import sys
sys.path.insert(0,".")
from AoCDecorator import AoC


class bingo:
    def __init__(self,x):
        self.card = np.array([y.split() for y in x]).astype(int)
        self.matches = np.array([[False]*5]*5)
        self.winner = False
        self.last = -1
    
    def checkcols(self):
        return any(sum(self.matches)==5)
    
    def checkrows(self):
        return any(sum(self.matches.T)==5)
    
    def check(self):
        self.winner = self.checkrows() or self.checkcols()
        return self.winner
    
    def draw(self,n):
         self.matches[np.where(self.card == n)] = True
         self.last = n
         self.check()
         return self.winner

    def score(self):
        return self.last*sum(self.card[np.logical_not(self.matches)])

class bingogame:
    def __init__(self,rows):
        nrows = len(rows)
        lst = [rows[6*i+1:6*(i+1)] for i in range(0,nrows//6)]

        self.cards = [bingo(x) for x in lst]
        self.len = len(lst)
        self.winner = -1
        self.loser = -1
        self.loser_pre = -1
    
    def draw(self,n):
        wins = [self.cards[i].draw(n) for i in range(0,self.len)]
        if self.winner == -1 and any(wins):
            self.winner = wins.index(True)
        
        if self.loser == -1 and all(wins):
            self.loser = self.loser_pre

        if self.loser_pre == -1 and self.len - sum(wins) == 1:
            self.loser_pre = wins.index(False)
    
    def score(self,part):
        if self.playing(part):
            print("No score available")
            return 0
        else:
            if part == 1:
                return self.cards[self.winner].score()
            if part == 2:
                return self.cards[self.loser].score()

    def playing(self,part):
        if part == 1:
            return self.winner == -1
        if part == 2:
            return self.loser == -1
    
    def play(self,draws,part):
        draws2 = [int(x) for x in draws.split(",")]
        i = 0

        while self.playing(part):
            self.draw(draws2[i])
            i +=1
            
        return self.score(part)



@AoC(2021,4)
def solve(data,part):
    bg = bingogame(data[1:])
    return bg.play(data[0],part)
    
if(__name__ == "__main__"):
    solve()

# Answer 1: 35711
# Answer 2: 5586