class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 0
        end = 1
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        while end != len(nums):
            
            if nums[end] == nums[start]:
                if end - start <= 1:
                    end += 1
                else:
                    
                    del nums[end]
                    
            else:
                start = end
                end += 1
        return len(nums)
        