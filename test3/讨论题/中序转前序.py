# 使用完全括号法，将下列中序表达式转换成前序表达式
# 中序转前序

from stack import Stack

# 根据一段字符串取第一个乘除实体
# 匹配括号
def findNextEntity(lis):
    res = ""
    opStack = Stack()#初始化栈
    for i in lis: #匹配左括号和右括号
        if i == "(":
            opStack.push(i)#左括号进栈
        elif i ==")":
            opStack.pop()#匹配到右括号就出栈一个左括号
        res += i #记录数据
        if opStack.isEmpty():#栈空就退出循环
            break
    if res=="":#是否记录到数据
        res = False
    return res

# 加括号
def addParentheses(expr):
    indexs = list()
    entities = list()
    
    i = 0 # 记录字符串添加进列表的长度
    while i<len(expr):
        if expr[i] in "+-*/":
            if expr[i] in "*/":
                # 得到列表中最后一个str
                tmp = entities[len(entities)-1] # (a+b)
                entities.remove(tmp) # 取出之后删除(a+b)
                # i+1,乘号前面字符串长度加上乘号的长度1，可以拿到乘号后面的str
                nextent = findNextEntity(expr[i+1:]) # c
                # 得到加括号之后的str
                entities.append("("+tmp+expr[i]+nextent+")") # '('+'(a+b)'+')'+'c'+')'
                i+=(len(nextent)+1) # 迭代i，控制循环退出
            elif expr[i] in "+-":
                indexs.append(expr[i])
                i+=1
        else:
            # 拿到乘号之前的str
            tmp = findNextEntity(expr[i:]) # (a+b)
            entities.append(tmp) #加入列表
            i += len(tmp) # 迭代i，记录加入列表的字符串长度
            
    while len(entities)>1:
        entities[0] = "(" + entities[0] + indexs[0] + entities[1] +")"
        indexs.remove(indexs[0])
        entities.remove(entities[1])
    
    return entities[0]

def infixToPrefix(infixexpr):
    # 完全括号法，根据计算机运算顺序每一步都加上括号
    infixexpr = addParentheses(infixexpr)
    result = []
    indexstack = Stack()
    lenexp = len(infixexpr) # 获取加括号后字符串的长度
    for i in range(lenexp):
        if infixexpr[i] == "(":
            indexstack.push(i)
            result.append("_")
        elif infixexpr[i] in "+-*/":
            result.append("_")
            result[indexstack.pop()] = infixexpr[i]
        elif infixexpr[i] == ")":
            result.append("_")
        else:
            result.append(infixexpr[i])
    while(result.count("_")):
        result.remove("_")
    return " ".join(result)


str = '(a+b)*c'
# print(findNextEntity(str))
# print(addParentheses(str))
print(infixToPrefix(str))