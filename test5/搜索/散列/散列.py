def hash(astring, tablesize):#利用序数值计算字符串的散列值
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos]*pos)
    return sum%tablesize
