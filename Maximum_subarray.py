class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = -10^5
        if len(nums) == 1:
            return nums[0]
        max_sum = -10^5
        max_sum_last = nums[-1]
        if max_sum_last > max_sum:
            max_sum = max_sum_last
            
        n = len(nums)
        for i in range(1,n):
            
            max_sum_last = max(nums[n-1-i],nums[n-1-i]+max_sum_last)
            if max_sum_last > max_sum:
                max_sum = max_sum_last
            # print(max_sum_last,max_sum)
            
        return max_sum