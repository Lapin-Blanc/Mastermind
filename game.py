import random

class MasterMind(object):
    def __init__(self):
        self.over = False
        self.id = str(id(self))
        self.tries = []
        self.code = [random.randint(0,5) for i in range(4)]
    
    def guess(self, guess):
        self.tries.append(guess)
        return self.check_guess(guess)
    
    def check_guess(self, guess):
        c = self.code[:]
        g = guess[:]
        black = 0
        white = 0
        nc = []
        ng = []
        for n,(i,j) in enumerate(zip(c,g)):
            if i==j:
                black += 1
            else:
                nc.append(i)
                ng.append(j)
        for n,i in enumerate(ng):
            if i in nc:
                white += 1
        if black == 4:
            self.over = True
        return (black, white)
    
    def __str__(self):
        return "%s" % self.code
