#有序列表顺序搜索
def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos<len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos]>item:
                stop = True
            else:
                pos +=1 
    return found
alist = [1,2,33,44,55]    
print(orderedSequentialSearch(alist,22))

#无序列表顺序搜索
def sequentialSearch(alist, item):
    pos = 0
    found = False
    while pos > len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos +=1
    return found            
alist = [1,2,33,44,55]    
print(sequentialSearch(alist,2))
