def partition(li,left,right):
    temp = li[left]#基准值
    while left<right:#左右都至少有一个数
        
        while left<right and li[right] >= temp:#从右往左找比基准值大的数
            right-=1
        li[left] = li[right]#找到小数之后放到基准数的空位上，基准数已经记录起来，覆盖掉也没啥

        while left<right and li[left] <= temp:#从左往右找比基准值大的数
            left+=1
        li[right] = li[left]#找到大数之后放到找小数时移空的right位置上

    li[left] = temp#把基准数放到小数的空位上
    return left #循环退出，左右下标碰头，一次排序结束，返回当前下标

def partition2(li,first,last):
    left,right = first+1,last
    temp = li[left]#基准值
    done = False
    while not done:#左右都至少有一个数
        
        while left<=right and li[right] >= temp:#从右往左找比基准值大的数
            right-=1
        while left<=right and li[left] <= temp:#从左往右找比基准值大的数
            left+=1
        if right<left:
            done = True
        else:
            li[left],li[right] = li[right], li[left]   
    li[first],li[right] = li[right], li[first]
    return left #循环退出，左右下标碰头，一次排序结束，返回当前下标

def quick_sort(li,left,right):
    if left<right:
        mid = partition2(li,left,right)
        quick_sort(li,left,mid-1)
        quick_sort(li,mid+1,right)
        
li = [5,7,4,6,3,1,2,9,8]
# print(partition2(li,0,len(li)-1))    
# print(partition2(li,0,len(li)-1))    
quick_sort(li,0,len(li)-1)
print(li)
