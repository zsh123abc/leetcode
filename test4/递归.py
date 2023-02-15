from turtle import *

# myTurtle = Turtle()
# myWin = myTurtle.getscreen()

# def dreawSpiral(myTurtle,linelen):
#     if linelen>0:
#         myTurtle.forward(linelen)
#         myTurtle.right(90)
#         dreawSpiral(myTurtle,linelen-5)

# dreawSpiral(myTurtle,100)
# myWin.exitonclick()        


# def recursive_fact(n):
#     if n<=1:
#         print(n)
#         return n
#     return n* recursive_fact(n-1)    

# n = 5
# print(recursive_fact(n))    


def listnum(alist):
    if len(alist)==1:#递归终止条件
        return alist[0]
    current = alist[0]#当前列表的第一位，切片递归后
    num = listnum(alist[1:])#切片使得每次列表都比之前少取一位
    return current+num

def listnum2(alist):
    return alist[0] if len(alist)== 1 else alist[0]+listnum2(alist[1:])  
alist = [1,2,18]
print(listnum2(alist))