from Node import Node
class UnorderedList:
    def __init__(self):
        self.head = None#初始化头节点，没有数据时为None

    def isEmpty(self):# 判断链表是否为空
        return self.head == None

    def add(self,item):#在链表头为链表添加新节点
        temp = Node(item)#创建新节点
        #将新节点从链表头添加进去

        temp.setNext(self.head)#新节点的下一个节点设置为当前的头节点
        self.head = temp#设置新头节点为新节点
        
   
    def length(self):#获取链表的长度
        current = self.head#链表的头节点
        count = 0#计数
        while current !=None:#节点为None就说明到最后一个节点
            count +=1#计数
            current = current.getNext()#迭代下一个节点
        return count  

    def search(self,item):#根据节点数据在链表中搜索节点
        current = self.head#获取链表头节点
        found = False#记录是否找到
        while current != None and not found:#not found找到对应的值就退出循环，不用在进行后面多余的步骤
            if current.data == item:#找到对应节点数据
                found = True#赋值为True退出循环
            else:
                current = current.getNext()#迭代下一个节点
        return found  

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

    def ergodic(self):#遍历链表
        current = self.head
        Nodelist = []
        while current != None:
            Nodelist.append(current.getData())
            current = current.getNext()
        return Nodelist

    def append(self,item):#在链表尾添加新节点
        node = Node(item)
        current = self.head
        p = True
        while p:
            if current.getNext() == None:#迭代到最后一个节点
                current.setNext(node)#将新节点添加到最后一个节点的后面
                p = False#控制循环退出
            else:
                current = current.getNext()#迭代下一个节点
        
    def insert(self,index,item):#在指定位置添加节点
        node = Node(item)
        current = self.head
        previous = None#记录当前节点
        if index < self.length():
            if index == 0:#在最开始加入节点
                node.setNext(self.head)
                self.head = node
            else:
                for i in range(index,0,-1):
                    if i == 1:
                        previous = current
                    current = current.getNext()
                # if current == None:
                #     return
                previous.setNext(node)
                node.setNext(current)
        else:
            print('链表长度不够')
    
    def pop(self):#删除链表最后一个节点，加入节点时是直接加入到头节点，所有直接删除头节点
        if self.isEmpty():
            print('链表为空')
            return
        current = self.head#获取当前头节点
        nextNode = current.getNext()#获取头节点的下一个节点
        self.head = nextNode#设置新头节点为nextNode，无引用指向旧头节点
        


    def pop(self,index):#删除链表指定位置节点
        if self.isEmpty():
            print('链表为空')
            return

        current = self.head
        previous = None
        for i in range(index):
            if current!=None:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()    
        else:
            previous.setNext(current.getNext())
        

mylist = UnorderedList()
mylist.add(14)
mylist.add(22)
mylist.add(5)
# mylist.append(98)
# mylist.append(99)
# mylist.add(97)
# mylist.add(96)
# len = mylist.length()
# print(len)
# s = mylist.search(56)
# # print(s)
# # mylist.remove(14)
# mylist.remove(5)
# # mylist.remove(5)
# # len = mylist.length()
# # print(len)
l = mylist.ergodic()
print(l)
# mylist.insert(index=0,item=10)

# mylist.pop(0)
# l = mylist.ergodic()
# print(l)