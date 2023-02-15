from Node import Node
class OrderdList:
    def __init__(self):
        self.head = None#初始化头节点，没有数据时为None
    def add(self,item):#在链表头为链表添加新节点
        temp = Node(item)#创建新节点
        #将新节点从链表头添加进去
        temp.setNext(self.head)#新节点的下一个节点设置为当前的头节点
        self.head = temp#设置新头节点为新节点
    def remove(self,item):#根据节点数据删除指定链表节点
        if self.isEmpty():#判断链表是否为空
            print('链表为空')
            return
        current = self.head#获取链表头节点
        previous = None#记录当前节点
        found = False
        while not found:
            if current.data == item:
                found = True
            else:
                previous = current#记录当前节点
                current = current.getNext()#迭代到下一个节点
        if previous == None:#等于None说明要删除的节点是链表的头一个节点
            self.head = current.getNext()#头节点指向当前节点的下一个节点
        else:
            #设置上一个节点的下一个节点为当前节点的下一个节点，
            #设置完就跳过了当前节点，没有任何引用指向当前节点，当前节点就失效了，删除节点完成
            previous.setNext(current.getNext())                  
    def search(self, item):#在列表中搜索 item。它接受一个元素作为参数，并且返回布尔值
        if self.isEmpty():
            print('链表中没有节点')
            return
        current = self.head#获取头节点
        while True:
            if current.getData() == item:#找到数据对应的节点，返回True
                return True
            else:#迭代节点
                if current.getNext()==None:#下一个节点为None时就走到末尾了，没找到对应节点，返回False
                    return False 
                else:# 不为None一值往后迭代节点
                    current = current.getNext()
    def isEmpty(self):
        return self.head == None
    def length(self):#获取链表的长度
        current = self.head#链表的头节点
        count = 0#计数
        while current !=None:#节点为None就说明到最后一个节点
            count +=1#计数
            current = current.getNext()#迭代下一个节点
        return count  
    def index(self,item):# 根据节点值找到该节点在链表中的位置
        if self.isEmpty():
            print('链表为空')
            return False
        current = self.head
        con = 0 # 记录节点在链表中的位置
        bool = True # 控制循环，找到
        while bool:
            if current.getData() == item:
                return con
            else:
                if current.getNext() != None:
                    current = current.getNext()
                    con+=1
                else:
                    bool = False
                    return bool    
    def pop(self):
        if self.isEmpty():
            print("链表为空")
            return -1
        current = self.head #获取头节点
        self.head = current.getNext() # 设置新头节点为要删除节点的下一个节点        
    def pop(self,index):#根据指定位置删除对应位置上的节点
        if self.isEmpty():
            print("链表为空")
            return -1
        if index >= self.length() or index < 0:
            print('下标越界')
            return -1
        current = self.head
        previous = None # 记录前一个节点

        while index > 0:
            if current.getNext()!=None:
                index-=1
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
            return current.getData()

        data = current.getData()#当前节点数据
        nextNode = current.getNext()#下一个节点
        previous.setNext(nextNode)#前一个节点的下一个节点变为当前节点的下一个节点，相当于跳过了当前节点
        return data
    def ergodic(self):#遍历链表
        list = []
        current = self.head
        while current != None:
            data = current.getData()
            current = current.getNext()
            list.append(data)
        print(list)

mylist = OrderdList()
mylist.add(21)
mylist.add(44)
mylist.add(66)
# mylist.ergodic()

# mylist.remove(66)

mylist.ergodic()
pop = mylist.pop(0)
print(pop)
mylist.ergodic()

# len = mylist.length()
# print(len)

# index = mylist.index(212)
# print(index)
# search = mylist.search(1)
# print(search)