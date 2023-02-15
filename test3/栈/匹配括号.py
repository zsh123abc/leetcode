from stack import Stack

def parChecher(string):
    stack = Stack() # 初始化栈
    balanced = True # 记录栈是否不为空
    index = 0 # 下标
    while index < len(string) and balanced: # 下标未越界，栈不为空
        str = string[index] # 从第一个开始取出字符串
        if str == '(': # 左括号添加进栈
            stack.push(str) #栈顶添加
        else: # 右括号就移除栈顶的左括号，匹配成功一个
            if stack.isEmpty(): # 栈为空就直接退出
                balanced = False
            else:
                stack.pop() # 删除栈顶元素

        index = index + 1 # 迭代下标
    stack.isEmpty
    # 栈为空说明全部两两匹配成功，一个左括号，一个右括号
    if stack.isEmpty() and balanced:
        return True
    else:
        return False
                
str = '()'
b = parChecher(str)               
print(b)