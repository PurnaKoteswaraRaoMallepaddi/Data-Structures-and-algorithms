class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        difference = 10000
        nums.sort()
        for i, num in enumerate(nums): 
            start,end = i+1,len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            while start < end:
                # print("main:", num, "start:",nums[start],"end:",nums[end])
                sum_ = nums[start] + num + nums[end]
                if abs(target - sum_) < abs(difference):
                    difference = (target - sum_) 
                    
                if sum_ < target:
                    start += 1
                elif sum_ > target:
                    end -= 1
                else:
                    return target - difference
        
                
        return target - difference