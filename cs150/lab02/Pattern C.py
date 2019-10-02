#Pattern C.py
#numbers arranged in a triangle
#
#Colin McCahill
#09/13/15

n=eval(input("Size:"))
for i in range(1,n+1):
    for j in range(i,n+1):
        print(j," ",sep='',end='')
    print()

    
