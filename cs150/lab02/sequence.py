#sequence.py
#lists the squares of all integers from some starting number squared down to one
#
#Colin McCahill
#09/10/15

x=eval(input("Give me a number to start with:"))
print("Squares from",x**2,"down to 1:")
for i in range(x,0,-1):
       print(i**2,", ",sep='',end='')
