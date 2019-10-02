#hello.py
#classic Hello, World program, but this time we will say hello from multiple
#processes
#
#Colin McCahill
#12/2/15

from multiprocessing import *

def HelloWorld(name):
    print("Hello to %s from process %d" %(name,current_process().pid))

def main():
    name=input("What is your name? ")
    n=eval(input("number n of processes to create: "))
    for i in range(n):
        p=Process(target=HelloWorld,args=(name,))
        p.start()
main()
