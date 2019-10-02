#PatternD.py
#print a weird triangle thing
#
#Colin McCahill
#09/13/15

n=eval(input("Size:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        for k in range(1,j+1):
            print(j," ",sep='',end='')
    print()
