#Pattern B.py
#numbers arranged in columns
#
#Colin McCahill
#09/12/15

n=eval(input("Size:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j," ",sep='',end='')
    print()
