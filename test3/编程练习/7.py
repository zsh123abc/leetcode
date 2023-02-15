class Deque:
    def __init__(self):
        self.items = []

    def addFront(self,item):#正面加入队列
        self.items.append(item)
    def removeFront(self):
        return self.items.pop()

    def addRear(self,item):
        self.items.insert(0,item)
    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        self.items == []

    def size(self):
        return len(self.items)

    def erg(self):
        for i in self.items:
            print(i,end=' ')

dq = Deque()
dq.addRear(1)

dq.removeRear()

dq.erg()
