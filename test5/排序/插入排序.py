def insertionSort(alist):#插入排序
    for i in range(len(alist)):
        currentvalue = alist[i]#要排序的单个数据
        position = i
        #当前下标>0并且前一位数大于后一位数，进入循环把前一位数往后移一位
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]#大的数据往后移
            position = position-1#大数据的下标也记录
        # 比要排序数大的数都往后移，直到比排序数小的数，当前位置就空了出来 
        alist[position] = currentvalue#把排序数放到空位置上，准备下一个数的排序

import time

start = time.perf_counter()
print(start)
alist = [4,2,1,6,7,2,1,0,1,1,1,1,3]
insertionSort(alist)
print(alist)
end = time.perf_counter()
print(end)
print(end-start)       