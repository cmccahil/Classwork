#hippo.py
#gives the hippo critter class
#
#Colin McCahill
#11/18/15

import critter
import color

class Hippo(critter.Critter):
    def __init__(self,x,y,steps):
        self.counter=0
        self.movement=steps

    def getStats(self):
        return (80,20)
    def getChar(self):
        return "H"
    def getColor(self):
        return color.BLUE
    def getMove(self,info):
        self.counter=self.counter+1
        if self.counter>self.movement*4:
            self.counter=1
        if self.counter<=self.movement:
            return critter.S
        elif self.counter<=self.movement*2:
            return critter.W
        elif self.counter<=self.movement*3:
            return critter.N
        elif self.counter<=self.movement*4:
            return critter.E
        
