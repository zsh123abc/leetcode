from turtle import *

myTurtle = Turtle()
myWin = myTurtle.getscreen()

def drawSpiral(myTurtle, lineLen):#递归画螺旋线
    if lineLen > 0:
        myTurtle.forward(lineLen)#向当前画笔方向移动lineLen像素长
        myTurtle.right(90)#顺时针移动90°,转弯90°
        drawSpiral(myTurtle,lineLen-5)

def drawSpiral2(myTurtle, lineLen):#循环画螺旋线
    lineLen = 100
    while lineLen>0:
        myTurtle.forward(lineLen)#向当前画笔方向移动lineLen像素长
        myTurtle.right(90)#顺时针移动90°
        lineLen -= 5


drawSpiral(myTurtle,100)
myWin.exitonclick()#画完保持窗口不关闭


