from queueText import Queue
def hotPotato(nameList, num):
    simqueue = Queue()
    for name in nameList:
        simqueue.enqueue(name)

    while simqueue.size() > 1: # 一直循环直到队列里的元素只有一个的时候
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue()) # 队列头的元素移到队列尾

        simqueue.dequeue() # 循环num次后移出队列头的元素

    return simqueue.dequeue() # 返回队列头的元素

p = hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 11)    
print(p)