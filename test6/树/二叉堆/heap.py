class Heap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    # 元素从最后往前面比对
    def precUp(self,i):#加入的节点在列表最后，传入列表长度，得到新加入的元素
        while i//2 > 0:#最小的元素放到堆顶
            if self.heapList[i] < self.heapList[i//2]:#当前节点比父节点小
                # 交换两个节点位置
                # self.heapList[node],self.heapList[node//2] = self.heapList[node//2],self.heapList[node]
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i//2#往父节点迭代    

    def insert(self, k):#插入元素
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.precUp(self.currentSize)

    # 元素从前面往往后比对
    def precDown(self,i):#最大的元素放到堆最底下
        while (i*2) <= self.currentSize:#i*2是i的左子节点，i*2+1是右子节点
            min = self.minChild(i)
            if self.heapList[i] > self.heapList[min]:
                # self.heapList[i],self.heapList[min] = self.heapList[min],self.heapList[i]
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[min]
                self.heapList[min] = tmp
            i = min
            
    def minChild(self, i):#找到最小的子节点
        if i*2+1 > self.currentSize:
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1  

    def delMin(self):#删除最小的节点
        retval = self.heapList[1]#获取最小的元素
        self.heapList[1] = self.heapList[self.currentSize] # 用最大的元素替换最小的元素
        self.currentSize = self.currentSize - 1 #列表长度-1
        self.heapList.pop()# 移除最后一个元素
        self.precDown(1)#重新排序 ，传入要排序元素的下标
        return retval#返回删除的元素


    def buildHeap(self,alist):#根据元素列表构建堆
        i = len(alist)//2
        self.currentSize = len(alist)
        self.heapList = [0]+alist[:]
        while i > 0:
            self.precDown(i)#每次排序一个
            i = i-1



if __name__ == '__main__':
    heap = Heap()
    # heap.insert(1)
    # heap.insert(2)
    # heap.insert(3)

    # min = heap.delMin()
    # print(min)
    # print(heap.heapList)

    l = [0,2,4,7,9]
    heap.buildHeap(l)
    print(heap.heapList)
    
