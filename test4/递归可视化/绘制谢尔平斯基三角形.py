from turtle import *
def drawTriangle(points, color, myTurtle):
      myTurtle.fillcolor(color)
      myTurtle.up()
      myTurtle.goto(points[0])#让指针对这绝对坐标画线
      myTurtle.down()
      myTurtle.begin_fill()#填充画完的三角形，画之前
      myTurtle.goto(points[1])
      myTurtle.goto(points[2])
      myTurtle.goto(points[0])
      myTurtle.end_fill()#填充画完的三角形，画之后

def getMin(p1,p2):
    return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)

def sierpinski(points, degree, myTurtle):
    colormap = ['blue', 'red', 'green', 'white', 'yellow',
                  'violet', 'orange']
    drawTriangle(points, colormap[degree], myTurtle)
    if degree > 0:
        sierpinski([points[0],
            getMin(points[0],points[1]),
            getMin(points[0],points[2])],degree-1,myTurtle)
        sierpinski([points[1],
            getMin(points[0],points[1]),
            getMin(points[1],points[2])],degree-1,myTurtle)
        sierpinski([points[2],
            getMin(points[2],points[1]),
            getMin(points[0],points[2])],degree-1,myTurtle)    
myTurtle = Turtle()
myTurtle.speed(0)
myWin = myTurtle.getscreen()
myPoints = [(-400, -200), (0, 400), (400, -200)]
print((myPoints[0][0]+myPoints[0][1])/2)
sierpinski(myPoints, 5, myTurtle)
myWin.exitonclick()
