#recpic.py
#This program should repeatedly prompt the user to pick a pattern, pick a size,
#and pick a depth of recursion and then display the appropriate picture. The
#patterns available to the user are Bubbles, Carpet, Gasket, Snowflake and Quit.
#When the user inputs "quit" instead of a pattern, your program should halt.
#
#Colin McCahill
#10/11/15

import picture

def bubbles(x,y,radius,depth,canvas):
    if depth==1:
        canvas.setFillColor(0,0,255)
        canvas.setOutlineColor(0,0,255)
        canvas.drawCircleFill(x,y,radius)
        canvas.display()
    else:
        canvas.setOutlineColor(0,0,255)
        canvas.setFillColor(0,0,255)
        canvas.drawCircleFill(x,y,radius)
        bubbles(x+radius,y+radius,(radius/2),depth-1,canvas)
        bubbles(x-radius,y+radius,(radius/2),depth-1,canvas)
        bubbles(x+radius,y-radius,(radius/2),depth-1,canvas)
        bubbles(x-radius,y-radius,(radius/2),depth-1,canvas)

def carpet(x,y,side,depth,canvas):
    if depth==1:
        canvas.setFillColor(255,0,0)
        canvas.setOutlineColor(255,0,0)
        canvas.drawSquareFill(x,y,side)
        canvas.display()
    else:
        canvas.setOutlineColor(255,0,0)
        canvas.setFillColor(255,0,0)
        canvas.drawSquareFill(x,y,side)
        carpet(x-(2/3)*side,y-(2/3)*side,side/3,depth-1,canvas)
        carpet(x+(1/3)*side,y-(2/3)*side,side/3,depth-1,canvas)
        carpet(x+(4/3)*side,y-(2/3)*side,side/3,depth-1,canvas)
        carpet(x+(4/3)*side,y+(1/3)*side,side/3,depth-1,canvas)
        carpet(x+(4/3)*side,y+(4/3)*side,side/3,depth-1,canvas)
        carpet(x+(1/3)*side,y+(4/3)*side,side/3,depth-1,canvas)
        carpet(x-(2/3)*side,y+(4/3)*side,side/3,depth-1,canvas)
        carpet(x-(2/3)*side,y+(1/3)*side,side/3,depth-1,canvas)

def gasket(a,b,c,d,e,f,depth,canvas):
    if depth==1:
        canvas.setFillColor(0,0,255)
        canvas.setOutlineColor(0,0,255)
        canvas.drawPolygonFill(((a,b),(c,d),(e,f)))
        canvas.display()
    else:
        canvas.setFillColor(0,0,255)
        canvas.setOutlineColor(0,0,255)
        gasket(a,b,(a+c)//2,(b+d)//2,(a+e)//2,f,depth-1,canvas)
        gasket((a+c)//2,(b+d)//2,c,d,(c+e)//2,(d+f)//2,depth-1,canvas)
        gasket((a+e)//2,b,(c+e)//2,(d+f)//2,e,f,depth-1,canvas)

def snowflake(x,y,side,depth,canvas):
    if depth==1:
        canvas.setPosition(x,y)
        canvas.setOutlineColor(0,255,0)
        canvas.rotate(-60)
        canvas.drawForward(side)
        canvas.rotate(120)
        canvas.drawForward(side)
        canvas.rotate(120)
        canvas.drawForward(side)
        canvas.display()
    else:
        canvas.setPosition(x,y)
        canvas.setOutlineColor(0,255,0)
        canvas.rotate(-60)
        drawLine(side,depth-1,canvas)
        canvas.rotate(120)
        drawLine(side,depth-1,canvas)
        canvas.rotate(120)
        drawLine(side,depth-1,canvas)

def drawLine(side,depth,canvas):
    d=side
    if depth==0:
        canvas.drawForward(side)
    else:
        drawLine(d//3,depth-1,canvas)
        canvas.rotate(-60)
        drawLine(d//3,depth-1,canvas)
        canvas.rotate(120)
        drawLine(d//3,depth-1,canvas)
        canvas.rotate(-60)
        drawLine(d//3,depth-1,canvas)
        
def main():
    print("Here are the options:")
    print("   Bubbles")
    print("   Carpet")
    print("   Gasket")
    print("   Snowflake")
    print("   Quit")
    done=False
    while not done:
    #t will stand for the type of design the user wants
        t=input("Which would you like? ")
        size=eval(input("Size: "))
        depth=eval(input("Depth: "))
        canvas=picture.Picture(size,size)
        print(t.lower())
        if t.lower()=="bubbles":
            canvas.setFillColor(255,125,0)
            canvas.drawRectFill(0,0,size,size)
            bubbles(size//2,size//2,size//4,depth,canvas)
        elif t.lower()=="carpet":
            canvas.setFillColor(0,255,0)
            canvas.drawRectFill(0,0,size,size)
            carpet(size//3,size//3,size//3,depth,canvas)
        elif t.lower()=="gasket":
            canvas.setFillColor(255,255,0)
            canvas.drawRectFill(0,0,size,size)
            gasket(0,size,size//2,0,size,size,depth,canvas)
        elif t.lower()=="snowflake":
            canvas.setFillColor(190,40,180)
            canvas.drawRectFill(0,0,size,size)
            snowflake(size//6,3*(size//4),(2/3)*size,depth,canvas)
            canvas.display()
        elif t.lower()=="quit":
            done=True
        else:
            print("That is not an option")
main()
