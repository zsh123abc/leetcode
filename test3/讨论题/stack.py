class Stack:
    def __init__(self):
        self.items = []

    # 将一个元素添加到栈的顶端。它需要一个参数 item，且无返回值
    def push(self,item):
        self.items.append(item)
    # 将栈顶端的元素移除。它不需要参数，但会返回顶端的元素，并且修改栈的内容
    def pop(self):
        return self.items.pop()
    # 返回栈顶端的元素，但是并不移除该元素。它不需要参数，也不会修改栈的内容
    def peek(self):
        return self.items[len(self.items)-1]
    # 检查栈是否为空。它不需要参数，且会返回一个布尔值
    def isEmpty(self):
        return self.items == []
    # 返回栈中元素的数目。它不需要参数，且会返回一个整数
    def size(self):
        return len(self.items)
