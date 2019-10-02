#mouse.py
#gives the mouse critter class
#
#Colin McCahill
#11/18/15

import critter
import color

class Mouse(critter.Critter):
    def __init__(self,x,y,color):
        self.counter=0
        pass
    def getStats(self):
        return (60,40)
    def getChar(self):
        return "M"
    def getColor(self):
        return color.getRandomColor()
    def getMove(self,info):
        self.counter=self.counter+1
        if self.counter%2==0:
            return critter.S
        else:
            return critter.E
    
