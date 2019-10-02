#colinm.py
#creates my own critter class
#
#Colin McCahill
#11/19/15

import critter
import color
import math

class ColinM(critter.Critter):
    def __init__(self,x,y):
        self.counter=0
    def getStats(self):
        return (59,41)
    def getChar(self):
        return "S"
    def getColor(self):
        return color.RED
    def getMove(self,info):
        for i in range(-2,3):
            for j in range(1,3):
                if info.getType(i,j)=='Lion':
                    return critter.C
        if info.getType(1,1)=='Hippo' or info.getType(1,1)=='Mouse' or info.getType(-1,1)=='Hippo':
            return critter.C
        elif info.getType(0,1)!='Stone' and info.getType(0,1)!='Chameleoturtle' and info.getType(0,1)!='ColinM' and info.getChar(0,1).isdigit()!=True:
            return critter.N
        elif info.getType(-1,0)!='Stone' and info.getType(-1,0)!='Chameleoturtle' and info.getType(-1,0)!='ColinM' and info.getChar(-1,0).isdigit()!=True:
            return critter.E
        elif info.getType(1,0)!='Stone' and info.getType(1,0)!='Chameleoturtle' and info.getType(1,0)!='ColinM' and info.getChar(1,0).isdigit()!=True:
            return critter.W
        else:
            return critter.C
        
