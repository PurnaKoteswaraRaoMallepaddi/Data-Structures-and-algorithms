class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        tuple = []
        
        nums.sort()
        done = []
        for i,target_ in enumerate(nums):
            if target_ not in done:
                done.append(target_)
                done_inner = []
                for j in range(i+1,len(nums)):
                    if nums[j] not in done_inner:
                        done_inner.append(nums[j])
                        start = j+1
                        end = len(nums) - 1

                        while end > start:
                            sum_ = nums[end] + nums[j] + nums[start]
                            if sum_ < -1*target_ + target:
                                start += 1
                            elif sum_ > -1*target_ + target:
                                end -= 1
                            else:
                                tuple.append([nums[end] , nums[j] , nums[start],
                                             target_])
                                start += 1
                                while nums[start] == nums[start-1] and start < end:
                                    start += 1
                
                            
        return tuple
                        
                        