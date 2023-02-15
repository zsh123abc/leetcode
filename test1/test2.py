# nums2 = []
# nums = [1,2,3,4,2,3]
# for i in range(len(nums)):
#     if nums[i] in nums2:
#         nums2.append(nums[i])
# print(nums2)

# grid = [[1,2,3],[4,5,6],[7,8,9]]

# for i in(range(len(grid))):
    
#     nums = 0
#     for i in grid[0]:
#         nums+=i
#     for i in grid[2]:
#         nums+=i    
#     num = nums+grid[1][1]

#     print(num)
# allowed = "ab"
# words = ["ad","bd","aaab","baa","badab"]
# for i in words:
#     if i in allowed:
#         print(i)

# nums = [2,5,5,11]
# target = 10

# def twoSum(nums,target):
#         h = {}
#         for i, v in enumerate(nums):#下标，数据
#             j = h.get(target - v, None)#字典查找key，key存在返回值，不存咋返回None
#             if j is not None:
#                 return [i, j]
#             h[v] = i
            
# print(twoSum(nums,target))        


def romanToInt(s):
        #几个特殊的罗马数字
        s = s.replace('IV','a')
        s = s.replace('IX','b')
        s = s.replace('XL','c')
        s = s.replace('XC','d')
        s = s.replace('CD','e')
        s = s.replace('CM','f')

        #所有罗马数对应的整数字典
        num = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'a':4,
               'b':9,'c':40,'d':90,'e':400,'f':900}
        
        #字典查找罗马数对应的整数
        total = 0
        for i in s:
            total += num[i]
        return total

print(romanToInt("III"))