def selectionSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        max = 0#记录最大值
        for i in range(1,passnum+1):
            if alist[i] > alist[max]:
                max = i
        alist[max],alist[passnum] = alist[passnum],alist[max]        
    print(alist)
alist = [122,233,33,44,55]  
selectionSort(alist)  