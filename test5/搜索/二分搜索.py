def binarySearch(alist, item):
    first = 0 # 开始
    last = len(alist) -1 # 结束
    found = False
    while not found and first <= last:
        mid = (first + last) // 2 # 中间值
        if alist[mid] == item:#先判断中间值是否是搜索数
            found = True
        else:#不是就二分在搜索
            if item < alist[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found
alist = [1,2,33,44,55]
print(binarySearch(alist,22))

def binarySearch2(alist, item):
    first = 0 # 开始
    last = len(alist) -1 # 结束
    found = False
    while not found and first <= last:
        mid = (first + last) // 2 # 中间值
        if alist[mid] == item:#先判断中间值是否是搜索数
            found = True
        else:#不是就二分在搜索
            if item < alist[mid]:
                return binarySearch2(alist[:mid],item)#左闭右开
            else:
                return binarySearch2(alist[mid+1:],item)
    return found
alist = [1,2,33,44,55]
print(binarySearch2(alist,2))   