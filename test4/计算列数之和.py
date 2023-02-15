def listnum(l):
    list = 0
    for num in l:
        list +=num
    return list
l = [1, 2, 3]
print(listnum(l))        


def listsum(numList):
    if len(numList) == 1:
        # print(numList[0])
        return numList[0]
    else:
        print(numList[0]+listsum(numList[1:]))
        return numList[0]+listsum(numList[1:])

print(listsum(l))
