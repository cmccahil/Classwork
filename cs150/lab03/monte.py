#monte.py
#This program calculates the value of Pi by simuolating the throwing of darts
#onto a round target on a square background.
#
#Colin McCahill
#09/17/15
import random
import math
n=eval(input('How many darts to throw?'))
hits=0

for i in range(n):
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    if math.sqrt(x*x+y*y)<=1:
        hits=hits+1
percent=abs((1-(4*hits/n)/(math.pi)))*100    
print('The value of Pi after ',n,' iterations is ', 4*hits/n,' which is off by ',"%4.2f" %percent,'%',sep='')

    

