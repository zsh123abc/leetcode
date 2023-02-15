# 希尔排序 也称 “递减增量排序”
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)
        print("After increments of size", sublistcount,"The list is", alist)    
        sublistcount = sublistcount//2

def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i]#记录当前数据
        position = i#当前下标
        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap
        alist[position] = currentvalue    


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shellSort(alist)
