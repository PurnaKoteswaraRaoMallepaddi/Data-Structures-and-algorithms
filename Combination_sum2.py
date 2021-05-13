class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sums_ = []
        candidates.sort()
        def finder(target,stack,candidates_):
            # print(target,stack,candidates_)
            if target == 0:
                sums_.append(stack)
                return
            elif target < 0:
                return
            i = 0
            while i < len(candidates_):
                
                # stack.append(val)
                if stack and stack[-1] > candidates_[i]:
                    i+=1
                    while i < len(candidates_) and candidates_[i] == candidates_[i-1]:
                        i+=1
                    continue
                else:
                    finder(target - candidates_[i], stack + [candidates_[i]], candidates_[:i] + candidates_[i+1:])
                i += 1
                while i < len(candidates_) and candidates_[i] == candidates_[i-1]:
                    i+=1
        finder(target,[],candidates)
        return sums_