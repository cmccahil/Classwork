#recnum.py
#prompt the user for integer n and integer k, compute n raised to power of k,
#compute sum of first n perfect squares, compute the value of n choose k
#
#Colin McCahill
#10/08/2015

def powers(n,k):
    if k==0:
        return 1
    else:
        return powers(n,k-1)*n

def sumofsquares(n):
    if n==1:
        return 1
    else:
        return sumofsquares(n-1)+n**2

def choose(n,k):
    if k>n:
        return 0
    if k==n:
        return 1
    if k==0:
        return 1
    else:
        return choose(n-1,k)+choose(n-1,k-1)
    
def main():
    print("Welcome to my Amazing Recursive Calculator!")
    print()
    n=eval(input("Please enter a non-negative integer n:"))
    k=eval(input("Please enter a non-negative integer k:"))
    print()
    print(n," raised to the power of ",k," is ",powers(n,k),".",sep='')
    print("The sum of the first ",n," squares is ",sumofsquares(n),".",sep='')
    print(n," choose ",k," is ",choose(n,k),".",sep='')

main()

