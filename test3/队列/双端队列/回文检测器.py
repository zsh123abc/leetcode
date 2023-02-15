from deque import Deque
def palchecker(str):
    deq = Deque()
    for i in str:
        deq.addFront(i)#把字符串从正面添加进队列

    stillEqual = True
    while deq.size() > 1 and stillEqual:
        firest = deq.removeFront()#从正面取出队列元素
        last = deq.removeRear()#从后面取出队列元素
        if firest != last:#前后比对，不相等就不是回文串
            stillEqual = False

    return stillEqual        

str = 'sartra'
p = palchecker(str)
print(p)