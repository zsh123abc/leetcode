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

class NodeList:
    def __init__(self,root):
        self.head = root

    def add(self,item):
        current = self.head
        node = Node(item)
        node.setNext(current)
        self.head = node

    def remove(self,item):
        found = False
        root = self.head
        parent = None
        while not found and root != None:
            if root.getData() == item:                   
                found = True
            else:
                parent = root
                root = root.getNext() 

        if parent != None:           
            parent.setNext(root.getNext())
        else:
            self.head = root.getNext()         

    def search(self,item):
        found = False
        root = self.head
        while not found and root != None:
            if root.getData() == item:                
                found = True
            else:
                root = root.getNext()
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

    def append(self,item):
        found = False
        current = self.head
        node = Node(item)
        while not found:
            if current.getNext() == None:
                current.setNext(node)
                found = True
            else:
                current = current.getNext()    

    def index(self,item):
        found = False
        root = self.head
        cound = 0
        while not found:
            if root == None:
                return -1
            if root.getData() == item:                
                found = True
            else:
                root = root.getNext()
            cound += 1 
        return cound

    def insert(self,pos,item):
        current = self.head
        node = Node(item)
        parent = None
        for i in range(pos):
            if current.getNext() != None:
                parent = current
                current = current.getNext()
        if parent != None:        
            parent.setNext(node)
            node.setNext(current)
        else:
            current = self.head
            node.setNext(current)
            self.head = node  
    
    def pop(self):
        current = self.head
        parent = None
        while True:
            if current.getNext()!=None:
                parent = current
                current = current.getNext()
            else:
                parent.setNext(None) 
                return current.getData()

    def pop(self,pos):
        current = self.head
        parent = None
        
        for i in range(pos):
            if current.getNext() != None:
                parent = current
                current = current.getNext()

        if current == self.head:
            self.head = current.getNext()
            return current.getData()

        nextnode = current.getNext()
        parent.setNext(nextnode)
        return current.getData()     

    def erg(self):
        nodeList = []
        current = self.head
        while current != None:
            nodeList.append(current.getData())
            current = current.getNext()
        return nodeList  

if __name__ == '__main__':
    root = Node(1)
    
    nodelist = NodeList(root)
    
    # nodelist.add(2)
    # nodelist.add(3)
    # nodelist.remove(3)
    # nodelist.append(2)
    # nodelist.append(3)
    # nodelist.insert(0,5)
    print(nodelist.pop(0))
    # print(nodelist.isEmpty())
    print(nodelist.length())
    # print(nodelist.search(2))
    print(nodelist.index(5))