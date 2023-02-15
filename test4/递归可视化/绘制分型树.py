from turtle import *

t = Turtle()
myWin = t.getscreen()

def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)#画线指针跟随
        t.right(20)
        tree(branchLen-15,t)#本次递归画出树往右的分支
        t.left(40)
        tree(branchLen-10,t)
        t.right(20)
        t.backward(branchLen)#画完树枝退到指针画之前的位置
        
t.speed(0)#修改画笔速度0为最大值，最小值为1
t.left(90)#指针向左移90°
t.up()#将笔从屏幕上拉起，拉起后画图屏幕不会显示
t.backward(300)#倒退往后画线，和forward是相反的
t.down()#将笔拉回屏幕，拉回后画图才会显示
t.color('green')#修改画笔颜色
tree(110,t)

myWin.exitonclick()#画完保持窗口不关闭