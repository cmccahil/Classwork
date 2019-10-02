#functionPractice.py
#prints the square of the number,if the number is even or odd,and the digits of
#the number reversed
#
#Colin McCahill
#09/24/15
import math
def main():
    done=False
    while not done:
        x=eval(input("x:"))
        if x==0:
            done=True
        else:
            print(square(x))
            checkEvenOdd(x)
            print(reverse(x))
            done=True

def square(x):
    return x*x
def checkEvenOdd(x):
    if x%2==0:
        print("Even")
    else:
        print("Odd")

def reverse(x):
    n=x
    rev=0
    #rev stands for the reverse number
    while n>0:
        rev=rev*10+n%10
        n=math.floor(n/10)
    return rev

main()
            
