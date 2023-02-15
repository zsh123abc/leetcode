from stack import Stack
def divideBy2(decNumber):
    stack = Stack()

    while decNumber > 0:
        rem = decNumber % 2 # 算得余数
        stack.push(rem) # 把余数加入栈顶
        decNumber = decNumber // 2 # 迭代成除2之后 

    binString = ''    
    while not stack.isEmpty(): # 不为空
        binString = binString + str(stack.pop())

    return binString

decNumber = 96
print(divideBy2(decNumber))    