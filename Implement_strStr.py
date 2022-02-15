class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Implement strStr()
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if needle == '':
            return 0
        
        for i,char in enumerate(haystack[:len(haystack)-len(needle) + 1]):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1