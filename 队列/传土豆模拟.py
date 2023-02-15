from queueText import Queue
def hotPotato(namelist, num):
    queue = Queue()
    for name in namelist:#先把所有数据放进队列
        queue.enqueue(name)

    while queue.size() > 1:#只剩最后一个人停止
        for i in range(num):#隔几个人就移几次
            queue.enqueue(queue.dequeue())#对头移除之后加入队尾
        queue.dequeue()#移除当前对头
    endnum = queue.dequeue()#返回队列剩下的最后一人
    return endnum
    

namelist = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
print(hotPotato(namelist,4))