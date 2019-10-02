#lion.py
#creates the Lion critter class
#
#Colin McCahill
#11/18/15

import critter
import color
import random

class Lion(critter.Critter):
    def __init__(self,x,y):
        self.counter=0

    def getStats(self):
        return (100,0)
    def getChar(self):
        return "L"
    def getColor(self):
        self.counter=self.counter+1
        if self.counter%2==0:
            return color.ORANGE
        else:
            return color.BLACK
    def getMove(self,info):
        if info.getChar(0,1)!='.' and info.getChar(0,1)!='S' and info.getChar(0,1)!='T' and info.getChar(0,1).isdigit()!=True:
            return critter.N
        elif info.getChar(-1,0)!='.' and info.getChar(-1,0)!='S' and info.getChar(-1,0)!='T' and info.getChar(-1,0).isdigit()!=True:
            return critter.E
        elif info.getChar(0,-1)!='.' and info.getChar(0,-1)!='S' and info.getChar(0,-1)!='T' and info.getChar(0,-1).isdigit()!=True:
            return critter.S
        elif info.getChar(1,0)!='.' and info.getChar(1,0)!='S' and info.getChar(1,0)!='T' and info.getChar(1,0).isdigit()!=True:
            return critter.W
        else:
            direction=[critter.N,critter.S,critter.E,critter.W]
            return direction[random.randint(0,3)]
            
        
