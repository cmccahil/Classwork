#patternA.py
#get a positive integer and print a square based on that number
#
#Colin McCahill
#09/12/15

n=eval(input("Size:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j," ",sep='',end='')
    print()
   
