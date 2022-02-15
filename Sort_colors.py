class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer_0 = 0
        pointer_2 = len(nums) - 1
        curr = 0
        while curr <= pointer_2:
            if nums[curr] == 0:
                nums[pointer_0],nums[curr] = nums[curr],nums[pointer_0]
                pointer_0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[pointer_2],nums[curr] = nums[curr],nums[pointer_2]
                pointer_2 -= 1
            else:
                curr += 1
        # for i,num in enumerate(nums):
        #     temp = i
        #     while temp >= 1 and num < nums[temp-1]:
        #         # print(temp)
        #         val = nums[temp]
        #         nums[temp] = nums[temp - 1]
        #         nums[temp - 1] = val
        #         temp = temp - 1
                
        