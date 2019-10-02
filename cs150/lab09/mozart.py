#mozart.py
#generates a random Minuet and Trio
#
#Colin McCahill
#11/16/15

import random
import soundwave

def main():
    #this is creating the mTable
    m=open("mTable.txt")
    mtable=[]
    row=[]
    rowCount=0
    for line in m:
        numbers=line.split()
        for i in numbers:
            row.append(i)
            rowCount=rowCount+1
            if rowCount==16:
                mtable.append(row)
                row=[]
                rowCount=0

    #minuet measures
    minuet=[]
    for j in range(16):
        minuet.append(mtable[random.randint(0,10)][j])
    music=soundwave.Soundwave()
    for k in minuet:
        minuetmeasure=soundwave.Soundwave("../Mfiles/M"+str(k)+".wav")
        music.concat(minuetmeasure)

    #creating tTable
    t=open("tTable.txt")
    ttable=[]
    row=[]
    rowCount=0
    for line in t:
        numbers=line.split()
        for i in numbers:
            row.append(i)
            rowCount=rowCount+1
            if rowCount==16:
                ttable.append(row)
                row=[]
                rowCount=0

    #trio measures
    trio=[]
    for j in range(16):
        trio.append(ttable[random.randint(0,5)][j])
    for k in trio:
        triomeasure=soundwave.Soundwave("../Mfiles/M"+str(k)+".wav")
        music.concat(triomeasure)
    #minuet measures (one last time)
    for k in minuet:
        minuetmeasure=soundwave.Soundwave("../Mfiles/M"+str(k)+".wav")
        music.concat(minuetmeasure)
    music.play()
    

main()
        
