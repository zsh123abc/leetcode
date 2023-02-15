class Queue:
    def __init__(self):
        self.items = []
        
    # 在队列的尾部添加一个元素。它需要一个元素作为参数，不返回任何值
    def enqueue(self, item):
        self.items.insert(0, item)
    # 从队列的头部移除一个元素。它不需要参数，且会返回一个元素，并修改队列的内容
    def dequeue(self):
        return self.items.pop()
    # 检查队列是否为空。它不需要参数，且会返回一个布尔值
    def isEmpty(self):
        return self.items == []
    # 返回队列中元素的数目。它不需要参数，且会返回一个整数
    def size(self):
        return len(self.items)

import random
def hotPotato(nameList):
    simqueue = Queue()
    for name in nameList:
        simqueue.enqueue(name)

    while simqueue.size() > 1: # 一直循环直到队列里的元素只有一个的时候
        num = random.randrange(1,10)#使用随机数
        print(num)
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue()) # 队列头的元素移到队列尾

        simqueue.dequeue() # 循环num次后移出队列头的元素

    return simqueue.dequeue() # 返回队列头的元素

p = hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"])
print(p)