#洗车队列
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

    