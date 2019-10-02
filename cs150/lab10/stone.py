#stone.py
#puts the stone in the critter world
#
#Colin McCahill
#11/18/15


import critter
import color

class Stone(critter.Critter):
    
    def getChar(self):
        return "S"
    
    def getColor(self):
        return color.GRAY
    
    def getMove(self, info):
        return critter.C
    
    def getStats(self):
        return 0, 100

    # we don't have a fightOver method here, because a 
    # Stone doesn't do anything with this information
    # i.e. it doesn't care to change the default behavior
