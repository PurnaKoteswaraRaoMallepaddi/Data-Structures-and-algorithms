class Solution(object):
    def my_func(self,list_):
        return list_[0]
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort(key = self.my_func)
        
        final = [intervals[0]]
        
        for i in range(1, len(intervals)):
            if final[-1][1] >= intervals[i][0]:
                temp = final[-1]
                final.append([min(final[-1][0],intervals[i][0]),max(final[-1][1],intervals[i][1])])
                final.remove(temp)
            else:
                final.append(intervals[i])
                
        return final
                
        