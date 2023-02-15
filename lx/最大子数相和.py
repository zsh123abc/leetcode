def maxSubArray(nums):
        """
        :type nums: List[int]
        :rtype: int
         """
        for i in range(1, len(nums)):
            nums[i]= nums[i] + max(nums[i-1], 0)
        return max(nums)

nums = [-5,-3,1,5,2,6]
print(maxSubArray(nums))        