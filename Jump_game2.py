class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        https://www.youtube.com/watch?v=cfdwhSmLt3w Solution
        """
        jumps = 1    #Here we are considering best of all the possible cases for the second jump 
        max_reach = nums[0]  # For the first number max reach is the same number
        curr_end = nums[0]   # Current end is the number it self 
        if len(nums) == 1 or nums[0] == 0:
            return 0
        
        for i in range(1,len(nums)):  #Considering we take the first jump, we need to find best max reach out of all the for second jump
            if i == len(nums)-1:      #final case
                return jumps 
            if i == curr_end:         #if we reach the all posibilities of first reach
                jumps += 1
                max_reach = max(max_reach,nums[i]+i)     # we will need to find max reach 
                curr_end = max_reach
            else:
                max_reach = max(max_reach,nums[i]+i)     
        
        
"""Solution using Recursion"""

#         self.min_steps = len(nums) + 1
#         def finder(start,steps,nums):
#             # print(start,steps,nums)
#             if start >= len(nums) - 1:
#                 if steps < self.min_steps:
#                     # print("here")
#                     self.min_steps = steps
#                 return
            
#             steps += 1
#             for i in range(start+1,start+nums[start]+1):
#                 # print(i)
#                 if start+nums[start] < len(nums) and nums[i]+i < start+nums[start]:
#                     print("skipped for ",i,start)
#                     continue
#                 finder(i,steps,nums)
                    
#         finder(0,0,nums)
                
#         return self.min_steps