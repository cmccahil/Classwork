#account.py
#there is an Account class, which simulates a bank account. there are methods to
#add and withrdrawmoneyfrom the account. There are multiple processes to act as
#users of this account. Each process will withdraw a random amount of money from
#the account, wait a random amount of time, and then add a random amount of
#money to the account.It will do this 3 times. They will each use their pid for
#the customer number.
#
#Colin McCahill
#12/2/2015

from multiprocessing import *
import random
import time

class Account:
    def __init__(self,rawvalue,lock):
        self.balance=rawvalue
        self.lock=lock
        
    def add(self,customer_number,amount):
        self.lock.acquire()
        self.balance.value=self.balance.value+amount
        print("Customer",customer_number,"added",amount,"balance",
              self.balance.value)
        self.lock.release()
        
    def withdraw(self,customer_number, amount):
        self.lock.acquire()
        if amount>self.balance.value:
            amount=self.balance.value
            self.balance.value=0
        else:
            self.balance.value=self.balance.value-amount
        print("Customer",customer_number,"removed",amount,"balance",
              self.balance.value)
        self.lock.release()

def Customer(money):
    for j in range(3):
        money.withdraw(current_process().pid,random.randint(0,100))
        time.sleep(random.randint(0,5))
        money.add(current_process().pid,random.randint(0,100))

def main():
    r=RawValue("i",100)
    myLock=Lock()
    money=Account(r,myLock)
    L=[]
    for k in range(5):
        p=Process(target=Customer,args=(money,))
        L.append(p)
    for p in L:
        p.start()

if __name__=="__main__":
    main()
    input()
    
               
    
    
        
        
        
    
