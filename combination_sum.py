class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sums_ = []
        candidates.sort()
        def finder(target,stack):
            if target == 0:
                sums_.append(stack)
                return
            elif target < 0:
                return
            for val in candidates:
                # stack.append(val)
                if stack and stack[-1] > val:
                    continue
                else:
                    finder(target - val, stack + [val])
        finder(target,[])
        return sums_
                