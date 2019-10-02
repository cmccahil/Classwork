#sketchy.py
#drawing of a forest
#
#Colin McCahill
#09/24/15

import picture
import random

canvas=picture.Picture(600,600)
canvas.setFillColor(150,255,0)
canvas.drawRectFill(0,0,600,600)

def tree():
    for i in range(100):
        x=random.randint(0,600)
        y=random.randint(0,600)
        canvas.setFillColor(0,255,0)
        canvas.drawPolygonFill([(x,y),(x+20,y),(x+30,y-20),(x+30,y-30),(x+20,y-40)
                     ,(x+10,y-40),(x-20,y-30),(x-20,y-20)])
        canvas.setFillColor(115,40,20)
        canvas.drawRectFill(x,y,5,40)
tree()
canvas.display()
input()
