from deque import Deque
def palchecker(aString):
    dq = Deque()
    for i in aString:#把字符串放入双端队列
        dq.addRear(i)

    stillEqual = True
    while dq.size() > 1 and stillEqual:
        rear = dq.removeRear()#从前端取出
        front = dq.removeFront()#从后端取出
        if rear != front:
            stillEqual = False
    return stillEqual

aString = 'cac'
print(palchecker(aString))