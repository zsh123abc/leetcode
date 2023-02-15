# 通过 散列 构建一个时间复杂度为 O(1)O(1) 的数据结构。
# 字典的增删改查的时间复杂度都是O(1),键值对结构，根据键直接找到值
class HashTable:
    def __init__(self):
        self.size = 11 #散列表初始长度
        self.slots = [None] * self.size #储存键
        self.data = [None] * self.size #储存值

    def put(self, key, data):
        hasvalue = self.hashfunction(key,len(self.slots))#获取散列值
        if self.slots[hasvalue] == None:#散列值对应的糟为空
            self.slots[hasvalue] = key
            self.data[hasvalue] = data
        else:#糟位已有值
            if self.slots[hasvalue] == key:#键相等
                self.data[hasvalue] = data#替换值              
            else:#键不想等
                nextlost = self.rehash(hasvalue,len(self.slots))#第一个糟
                while self.slots[nextlost] != None and self.slots[nextlost] != key:
                    nextlost = self.rehash(nextlost, len(self.slots)) #糟不为空，且键不想等就再找下一个糟
                if self.slots[nextlost] == None:#当前糟位为空
                    self.slots[nextlost] = key#存放键值
                    self.data[nextlost] = data
                else:#槽位不为空，就说明键相等
                    self.data[nextlost] = data#替换键对应的值
   
    def rehash(self, oldhash, size):#顺序搜索空槽
        return(oldhash+1)%size # %size是为了不让很多键值存放到一堆，分散糟位
    def hashfunction(self,key, size):#利用序数值计算字符串的散列值
        return key%size

    def get(self, key):
        startslot = self.hashfunction(key,len(self.slots))#获取数据对应的散列值
        data = None#记录value
        found = False#循环终止条件
        stop = False#循环终止条件
        position = startslot #新赋值一个记录散列值，保留住最开始的散列值
        while not found and not stop and self.slots[position] != None:#当前散列值对应的槽位有数据
            if self.slots[position] == key:#当前糟位数据的键key是否和要获取的键一样
                data = self.data[position]#一样直接通过键找到值
                found = True#终止循环
            else:#当前散列值对应的槽位没有数据
                position = self.rehash(position,len(self.slots))#寻找其他槽位
                if position == startslot:#找到开始的槽位就代表找完所有糟位了
                    stop = True#终止循环
        return data#返回数据，有数据就是值，没有就是None

    def __getitem__(self, key):#迭代映射，可以让对象实现迭代功能
        return self.get(key)
    def __setitem__(self, key, data):#方便赋值，可以直接键值赋值 HashTable[key]=val
        self.put(key,data)


if __name__ == '__main__':
    tabel = HashTable()
    tabel[54] = 'cat' #重写了__setitem__函数，可以实现键值直接赋值
    tabel[26] = 'dog'
    tabel[66] = 'pig'
    tabel[44] = 'bird'

    print(tabel.slots)#输出散列表中的所有数据
    # 重写了__getitem__函数，可以直接通过键获取到值
    print(tabel[28])#通过键访问值