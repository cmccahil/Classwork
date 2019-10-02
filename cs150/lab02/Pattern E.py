#Pattern E
#Print a large "E" made out of stars
#
#Colin McCahill
#09/13/15

n=eval(input("Size:"))
for i in range(1,n+3):
    print("*",sep='',end='')
print()

for j in range(1,n+1):
    print("*")

for k in range(1,n+2):
    print("*",sep='',end='')
print()

for l in range(1,n+1):
    print("*")

for m in range(1,n+3):
    print("*",sep='',end='')
