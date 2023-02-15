from stack import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        sym = symbolString[index]
        if sym in "([{":
            s.push(sym)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,sym):
                    balanced = False
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False


def matches(open,close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)

s = '[(]{)}'
print(parChecker(s))        