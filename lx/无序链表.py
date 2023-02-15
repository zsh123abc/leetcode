class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def getNext(self):
        return self.next
    def setNext(self, nextNode):
        self.next = nextNode
    def getData(self):
        return self.data
    def setData(self, newdata):
        self.data = newdata       

    
class Nodelist:
    def __init__(self, root):
        self.head = root

    def add(self, item):#从链表头加入元素
        node = Node(item)
        node.setNext(self.head)
        self.head = node
        
    def remove(self, item):#删除链表末尾的元素
        if self.isEmpty():
            return None
        
        if self.head.getData() == item:
            self.head = self.head.getNext()
            return True

        root = self.head
        found = False
        parent = None
        while not found:
            if root.getNext() == None:
                found = True
            else:
                parent = root 
                root = root.getNext()
                if root.getData() == item:
                    parent.setNext(root.getNext())

    def search(self, item):#在链表中搜索元素，返回是否
        if self.isEmpty():
            return None

        root = self.head
        found = False

        while not found:
            if root.getData() == item:
                found = True
            else:
                if root.getNext() == None:
                    return False
                else:
                    root = root.getNext()    
        return found

    def append(self, item):#在链表末尾添加元素
        if self.search(item):
            return
        node = Node(item)
        root = self.head
        while True:
            if root.getNext() == None:
                root.setNext(node)
                break
            else:
                root = root.getNext()    

    def index(self, item):#在链表中搜索元素，返回下标
        if self.isEmpty():
            return None

        root = self.head
        found = False
        cound = 1
        while not found:
            if root.getData() == item:
                found = True
            else:
                if root.getNext() == None:
                    return False
                else:
                    root = root.getNext()
                    cound += 1 
        return cound

    def insert(self, pos, item):#在链表指定位置插入元素
        if self.search(item):
            return None

        root = self.head
        parent = None
        node = Node(item)
        for i in range(pos):
            if i == pos-1:
                parent = root
            root = root.getNext()
        parent.setNext(node)
        node.setNext(root)  

    def isEmpty(self):#判断链表是否为空
        return self.head == None

    def length(self):#获取链表长度
        if self.isEmpty():
            return 0
        root = self.head
        count = 0
        while root != None:
            count+=1    
            root = root.getNext()
        return count

    def pop(self):#移除链表最后一位元素，返回移除的元素
        if self.isEmpty():
            return -1
        root = self.head    
        cound = 0
        parent = None
        while root.getNext() != None:  
            parent = root  
            root = root.getNext()
            cound += 1
        parent.setNext(None)
        return cound

    def pop(self, pos):#移除链表指定位置的元素，返回移除的元素
        if self.isEmpty():
            return -1
        root = self.head
        parent = None
        if pos == 0:
            self.head = root.getNext()
            return root
        for i in range(pos):
            if i == pos-1:
                parent = root
            root = root.getNext()

        parent.setNext(root.getNext())
        return root

if __name__ == '__main__':
    root = Node(1)
    nodelist = Nodelist(root)
    nodelist.add(2)
    nodelist.add(3)
    # nodelist.append(5)
    # nodelist.insert(1,6)
    print(nodelist.pop(0).getData())

    # print(nodelist.length())
    print(nodelist.search(3))
    # print(nodelist.index(5))
    