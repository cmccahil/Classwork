#chameleoturtle.py
#creates the chameoturtle critter class
#
#Colin McCahill
#11/19/15

import critter
import color
import math

class Chameleoturtle(critter.Critter):
    def __init__(self,x,y):
        self.newcharacter="T"
        self.newcolor=color.GREEN
    def getStats(self):
        return (50,50)
    def getChar(self):
        return self.newcharacter
    def getColor(self):
        return self.newcolor
    def getMove(self,info):
        for i in range(-3,4):
            for j in range(-3,4):
                if math.sqrt(i**2+j**2)<=3:
                    if info.getType(i,j)!='.' and info.getType(i,j)!='Stone' and info.getType(i,j)!='Chameleoturtle' and info.getType(i,j).isdigit()!=True:
                        return critter.C
        return critter.N

    def fightOver(self,kill,oppFight):
        self.newcharacter=oppFight.getChar()
        self.newcolor=oppFight.getColor()
