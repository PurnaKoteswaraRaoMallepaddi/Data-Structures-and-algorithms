class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.final = []
        def permu(curr,rem):
            print(curr,rem)
            if len(rem) == 0:
                self.final.append(curr)
                return
            else:
                for i,val in enumerate(rem):   
                    permu(curr + [val],rem[:i]+rem[i+1:])
        nums.sort()
        permu([],nums)
        return self.final
        