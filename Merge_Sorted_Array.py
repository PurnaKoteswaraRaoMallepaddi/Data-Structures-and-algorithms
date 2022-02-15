class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        The s30 solution.
        """

        end = len(nums1) - 1
        max1 = m-1
        max2 = n-1
        while max2 >= 0 and max1 >= 0:
            if nums1[max1] >= nums2[max2]:
                nums1[end] = nums1[max1]
                end -= 1
                max1 -= 1
            elif nums1[max1] < nums2[max2]:
                nums1[end] = nums2[max2]
                end -= 1
                max2 -= 1
        if max2 >= 0:
            while end >= 0 and max2 >= 0:
                nums1[end] = nums2[max2] 
                end -= 1
                max2 -= 1
        # for i in range(len(nums1)-n,len(nums1)):
        #     nums1[i] = nums2[i - m]
        # del nums2
        # curr = len(nums1)-n
        # while curr < len(nums1):
        #     end = curr - 1
        #     while end >= 0 and nums1[end] > nums1[end + 1]:
        #         nums1[end],nums1[end+1] = nums1[end + 1],nums1[end]
        #         end -= 1
        #     curr += 1
        