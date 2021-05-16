class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        final = []
        
        intervals.sort(key = lambda x:x[0])
        
        final.append(intervals[0])
        for i in range(1,len(intervals)):
            if final[-1][1] >= intervals[i][0] :
                final[-1][1] = max(intervals[i][1],final[-1][1])
            else:
                final.append(intervals[i])
        return final