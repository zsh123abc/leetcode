from stack import Stack
mystack = Stack()
# def toStr(n, base):
#     convString = "0123456789"
#     if n < base:#停止递归的条件
#         return convString[n]#返回拆分后的数
#     return convString[n%base] + toStr(n//base,base)#递归向正确方向靠近

# print(toStr(769,2))


def toStr(n, base):
    convString = "0123456789"
    if n < base:#停止递归的条件
        mystack.push(convString[n])
    else:
        mystack.push(convString[n%base])
        toStr(n//base,base)#递归向正确方向靠近

toStr(769,10)
while not mystack.isEmpty():
    print(mystack.pop())