class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,data):
        self.data = data
    def setNext(self,newnext):
        self.next = newnext


class OrederdList:
    def __init__(self,root):
        self.head = root

    def add(self,item):
        node = Node(item)
        current = self.head
        found = False
        parent = None

        while not found and current != None:
            if current.getData()<item:
                parent = current
                current = current.getNext()
            else:         
                found = True
        if parent:
            parent.setNext(node)
            node.setNext(current)
        else:
            node.setNext(current)
            self.head = node

    def remove(self,item):
        current = self.head
        found = False
        parent = None
        while current.getData() != item:
            parent = current
            current = current.getNext()
        parent.setNext(current.getNext())    

    def search(self,item):
        current = self.head
        found = False
        stop = False
        while not found and not stop and current != None:
            if current.getData() == item:
                found = True
            else:
                if item < current.getData():
                    stop = True
                else:
                    current = current.getNext()    
        return found

    def isEmpty(self):
        return self.head == None

    def length(self):
        current = self.head
        cound = 0
        while current != None:
            cound += 1
            current = current.getNext()     
        return cound

    def index(self,item):
        current = self.head
        found = False
        cound = 1
        while not found and current != None:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                cound += 1
        return cound

    def pop(self):
        current = self.head
        found = False
        parent = None
        while not found:
            if current.getNext() != None:
                parent = current
                current = current.getNext()
            else:
                parent.setNext(None)
                found = True
        return current.getData()          

    def pop(self,pos):
        current = self.head
        parent = None
        for i in range(1,pos):
            parent = current
            current = current.getNext()
        if parent:    
            parent.setNext(current.getNext()) 
        else:
            self.head = current.getNext()      
        return current.getData()
            
    def erg(self):
        nodeList = []
        current = self.head
        while current != None:
            nodeList.append(current.getData())
            current = current.getNext()
        return nodeList    



if __name__ == '__main__':
    root = Node(11)
    nodelist = OrederdList(root)
    nodelist.add(87)
    # nodelist.add(4)
    nodelist.add(3)
    nodelist.add(22)
    nodelist.add(33)
    # nodelist.remove(3)
    print(nodelist.search(36))
    # print(nodelist.index(3))
    # print(nodelist.pop())
    # print(nodelist.pop(1))
    print(nodelist.erg())
    # print(nodelist.length())