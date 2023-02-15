class Node:
    def __init__(self, data):
        self.data = data
        self.head = None
    def getNext(self):
        return self.next
    def setNext(self, nextNode):
        self.next = nextNode
    def getData(self):
        return self.data
    def setData(self, newdata):
        self.data = newdata 


class NodeList:
    def __init__(self):
        self.head = None
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

    def search(self,item):
        if self.isEmpty():
            return


    def add(self,item):
        current = self.head     
        node = Node(item)
        pre = None
        while True:
            if self.head == None:
                self.head = node
                break
            else:
                if current.getData()<item:
                    pre = current
                    current = current.getNext()
                else:                
                    pre.setNext(node)
                    node.setNext(current)      


if __name__ == '__main__':
    nodelist = NodeList()                    
    nodelist.add(1)
    # nodelist.add(2)
    print(nodelist.length())