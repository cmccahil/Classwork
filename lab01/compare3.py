#compare3
#This modifies program compare2 and puts 3 numbers in increasing order instead of 2
#
#Colin McCahill
#09/03/15

x=eval(input("Enter one number:"))
y=eval(input("Enter a second number:"))
z=eval(input("Enter a third number:"))
if (x<=y) and (y<=z):
    print(x,y,z)
elif (x>=y)and(x<=z):
    print(y,x,z)
elif(x<=z)and(z<=y):
    print(x,z,y)
elif(x>=z)and(x<=y):
    print(z,x,y)
elif(y>=z)and(y<=x):
    print(z,y,x)
elif(y<=z)and(y<=x):
    print(y,z,x)
