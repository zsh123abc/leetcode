from stack import Stack

def divideBy2(decNumber,base):
    digits = '0123456789ABCDEF'
    stack = Stack()
    num = 0
    baselist = []
    while decNumber > 0:
        num = decNumber%base
        stack.push(num)
        decNumber = decNumber//base
        print(decNumber)
    string =''
    while not stack.isEmpty():
        string = string+str(digits[stack.pop()])
    return string    


number = 17
print(divideBy2(number,2))