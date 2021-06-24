class Solution(object):
    def divide(self, dividend, divisor):
        """
        29 problem
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        neg=( (dividend < 0) != (divisor < 0) )
        dividend = abs(dividend)
        divisor = abs(divisor)
        ans = 0
        inc = 1
        while dividend >= divisor:
            dividend -= divisor
            ans += inc
            inc += inc
            divisor += divisor
            if divisor > dividend:
                
                divisor = divisor / inc
                inc = 1
        if neg:
            return max(-1*ans,-2147483648)
        else:
            return min(ans,2147483647)
         
#         count = 0
#         sign = 0
        
#         if dividend < 0 and divisor < 0:
            
#             dividend = -1*dividend
#             divisor = -1*divisor
#             count = min(int(dividend/divisor),2147483647)
#             return count
#         elif divisor < 0:
#             divisor = -1*divisor
#             count = min(int(dividend/divisor),2147483648)
#             return -1*count
#         elif dividend < 0:
#             dividend = -1*dividend
#             count = min(int(dividend/divisor),2147483648)
#             return -1*count
            
        