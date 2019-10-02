#syracuse.py
#This contains a recursive function rec(x) that takes in an integer x and
#returns an integer indicating the number of elemnets in the Syracuse sequence
#that begins with x (counting the starting number x and the final number 1).
#
#Colin McCahill
#11/4/2015

def rec(x):
    if x==1:
        return 1
    elif x%2==0:
        x=x//2
        return 1+rec(x)
    else:
        x=3*x+1
        return 1+rec(x)
    
def main():
    done=False
    lengthneeded=eval(input("Syracuse Sequence Length(positive integer):"))
    sequencelength=0
    startingvalue=0
    while sequencelength<lengthneeded:
        startingvalue=startingvalue+1
        sequencelength=rec(startingvalue)
    print("The necessary starting value in order to get a sequence the length of", lengthneeded,"is",startingvalue)
main()
        
