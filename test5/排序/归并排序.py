def mergeBort(alist):
    print("分解 ", alist)
    if len(alist) > 1:
        mid = len(alist)//2#对半分
        left = alist[:mid]#记录左边一半
        right = alist[mid:]#记录右边一半
        mergeBort(left)#递归拆分左边，拆成只剩一个元素
        mergeBort(right)#递归拆分右边
        print(left,right)
        i,j,k=0,0,0
        while i<len(left) and j<len(right):#下标不能越界
            if left[i] < right[j]:#i比j小
                alist[k] = left[i]#k记录小的
                i = i + 1
            else:#j比i小
                alist[k] = right[j]#j小，把j往前移，覆盖大的元素位置
                j = j + 1    
            k = k + 1#k下标也往后移

        while i < len(left):
            alist[k] = left[i]#大的放到后面
            k += 1
            i += 1   
        while j < len(right):
            alist[k] = right[j]
            k += 1
            j += 1
    print("合并 ", alist)


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeBort(alist)    