import copy

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        ref_matrix = copy.deepcopy(matrix)
        for i in range(n):
            for j in range(len(matrix[i])):
                matrix[i][j] = ref_matrix[n-j-1][i]
                
                