class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_product = nums[0]
        max_product = nums[0]
        max_final = nums[0]
        print(max_product)
        for i in range(1,len(nums)):
            temp1 = nums[i]*min_product
            temp2 = nums[i]*max_product
            min_product = min(nums[i],temp1,temp2)
            max_product = max(nums[i],temp1,temp2)
            print(max_product,nums[i],nums[i]*min_product,nums[i]*max_product)
            if max_product > max_final:
                max_final = max_product
        return max_final
        