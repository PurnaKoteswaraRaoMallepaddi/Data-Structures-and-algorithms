class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = nums[0]
        curr_end = nums[0]
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        
        for i in range(1,len(nums)):
            if i == len(nums)-1:
                return True
            if i == curr_end:
                max_reach = max(max_reach,nums[i]+i)
                
                if nums[i] == 0 and max_reach == curr_end:      #for [2,5,0,0] scenario
                    return False
                curr_end = max_reach
            else:
                max_reach = max(max_reach,nums[i]+i)
                
        return False