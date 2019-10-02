#monte.py
#asks user how many processes to use, prints out approximate value of pi based
#on 100,000,000 throws divided among those processes. should print how long it
#took
#
#Colin McCahill
#12/2/2015

from multiprocessing import *
import random
import math
import time

def oldmonteprogram(darts):
    hits=0
    for i in range(darts):
        x=random.uniform(-1,1)
        y=random.uniform(-1,1)
        if math.sqrt(x*x+y*y)<=1:
            hits=hits+1
    return hits
    
def main():
    darts=eval(input('How many darts to throw? '))
    n=eval(input("How many processes would you like to use? "))
    start=time.time()
    lessdarts=[]
    for i in range(n):
        lessdarts.append(darts//n)
    for j in range(darts%n):
        lessdarts[j]=lessdarts[j]+1
    pool=Pool(processes=n)
    results=pool.map(oldmonteprogram, lessdarts)
    hits=0
    for k in results:
        hits=hits+k
    end=time.time()
    elapsed=end-start
    percent=abs((1-(4*hits/darts)/(math.pi)))*100
    print('The value of Pi after ',darts,' iterations is ', 4*hits/darts,
          ' which is off by ',"%4.2f" %percent,'%. It took ',elapsed,
          ' seconds to run this program with ',n,' processes.',sep='')
    
main()
