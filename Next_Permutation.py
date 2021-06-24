class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        https://www.youtube.com/watch?v=quAS1iydq7U
        """
        for i in range(2,len(nums)+1):
            if nums[len(nums) - i] < nums[len(nums) - i + 1]:
                index1 = len(nums) - i
                index2 = nums[index1+1:].index(min([val for val in nums[index1+1:] if val > nums[index1]]))
                
                index2 = index2 + index1 + 1
                print(index2)
                temp = nums[index2]
                nums[index2] = nums[index1]
                nums[index1] = temp
                swap_ind = int((len(nums) - index1)/2)
                temp1 = nums[index1+1:]
                temp1.sort()
                for j in range(index1+1,len(nums)):
                    nums[j] = temp1[j - (index1+1)]
                # for j in range(1,swap_ind+1):
                #     temp = nums[index1 + j]       #first i tried reversing the right side part, but then got an idea of just sorting the right part so the above soution
                #     nums[index1 + j] = nums[-1*j]
                #     nums[-1*j] = temp
                return
        nums.sort()
                    
        
        
        
        
        
#         self.this = False
#         self.len_nums = len(nums)
#         self.final = []
#         self.given = nums[:]
#         def permu(curr,rem):
            
#             if len(rem) == 0:
#                 print(curr,rem,self.given)
#                 if self.this:
                    
#                     self.final = curr
#                     self.this = False
#                 if self.given == curr:
#                     print(curr,rem,self.given)
#                     self.this = True
                
#                 return
#             rem.sort()
#             for i,val in enumerate(rem):
#                 permu(curr+[val],rem[:i]+rem[i+1:])
        
#         nums.sort()
#         permu([],nums)
#         if len(self.final) == len(nums):
            
#             for i in range(len(nums)):
#                 nums[i] = self.final[i]