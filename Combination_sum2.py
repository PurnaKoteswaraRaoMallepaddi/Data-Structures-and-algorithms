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
            if target == 0:           #This is for when we achive what we wanted
                sums_.append(stack)
                return
            elif target < 0:          # When the target is coming to be negative
                return
            i = 0
            while i < len(candidates_):    #Here while loop because we want to parse through when there is same numbe ragain
                
                # stack.append(val)
                if stack and stack[-1] > candidates_[i]:   #This is because to remove viceversa cases such as [2,5] and [5,2]
                    i+=1
                    while i < len(candidates_) and candidates_[i] == candidates_[i-1]:  #Pasing through similar cases
                        i+=1
                    continue
                else:
                    finder(target - candidates_[i], stack + [candidates_[i]], candidates_[:i] + candidates_[i+1:])   #recursion
                i += 1
                while i < len(candidates_) and candidates_[i] == candidates_[i-1]:   #Pasing through similar cases
                    i+=1
        finder(target,[],candidates)   #Initial Call
        return sums_