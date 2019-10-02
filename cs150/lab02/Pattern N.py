#Pattern N
#Making an N out of Stars
#
#Colin McCahill
#09/13/15

n=eval(input("Size:"))
print("*",sep='',end='')
for i in range(1,n+1):
    print(" ",sep='',end='')
print("*")

for j in range(1,n+1):
    print("*",sep='',end='')
    for k in range(1,j):
        print(" ",sep='',end='')
    print("*",sep='',end='')
    for l in range(0,n-j):
        print(" ",sep='',end='')
    print("*",sep='',end='')
    print()

print("*",sep='',end='')
for m in range(1,n+1):
    print(" ",sep='',end='')
print("*")


    
