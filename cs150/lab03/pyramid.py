#pyramid.py
#get a number width from the user, as well as the number of bricks tall to make
#the pyramid(n).
#
#Colin McCahill
#09/17/15

import picture 
width=eval(input("What is the width of the canvas?"))
n=eval(input("How many bricks tall is the pyramid?"))
canvas=picture.Picture(width,width)
canvas.setFillColor(0,255,255)
canvas.drawRectFill(0,0,width,width)
sidelength=width/n

for i in range(0,n):
    for j in range (n-i):
        startY=(width-(i+1)*(sidelength))
        startX=((i*(1/2)*sidelength)+sidelength*j)
        canvas.setFillColor(255,255,0)
        canvas.drawRectFill(startX,startY,sidelength,sidelength)
    
    
canvas.display()
input()
