#fibonacci
#Compute and ouptut the nth Fibonacci number.
#
#Colin McCahill
#09/10/15

print("My incredible Fibonacci generator!")
n=eval(input("Please enter an integer:"))
a=1
b=1
for i in range(n-2):
    c=a+b
    a=b
    b=c
print("The ",n,"th number in the Fibonacci sequence is ",b,sep='')

