#primes.py
#get a number n from user that represents the number of primes to print out
#output the first n primes, and the number of twin primes amongst these n
#
#Colin McCahill
#09/20/15

maxCount=eval(input("How many primes?"))
count=0
n=2
twin=0
print("The first",maxCount,"primes are:")
while count<maxCount:
    isPrime=True
    for i in range(2,n):
        if n%i==0:
            isPrime=False
    if isPrime:
        print(n,"",end='')
        count=count+1
        if n==2:
            previousn=n
        if n-2==previousn:
            twin=twin+1
        previousn=n
    n=n+1
print()
print("Amongst these there are",twin,"twin primes.")

            
