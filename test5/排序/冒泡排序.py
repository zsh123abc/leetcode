def bubbleSort(alist):#循环冒泡排序
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] >alist[i+1]:
                # temp = alist[i]
                # alist[i] = alist[i+1]
                # alist[i+1] = temp
                alist[i],alist[i+1] = alist[i+1],alist[i]
    print(alist)
alist = [122,233,33,44,55]   
bubbleSort(alist)  

def shortBubbleSort(alist):#递归冒泡排序
    exchanges = True
    passnum = len(alist)-1
    while exchanges and passnum > 0:
        exchanges = False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                exchanges = True
                alist[i],alist[i+1] = alist[i+1],alist[i]
    print(alist)
alist = [122,233,33,44,55]   
shortBubbleSort(alist)  
