class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        min_row = 0
        max_col = len(matrix[0]) - 1
        
        while min_row < len(matrix) and max_col >= 0:
            print(matrix[min_row][max_col])
            if matrix[min_row][max_col] == target:
                return True
            elif matrix[min_row][max_col] < target:
                min_row += 1
            else:
                max_col -= 1
        return False
#     def binary_search(self,matrix,ind,target):
#         st = 0
#         en = len(matrix[ind]) - 1
#         while st <= en:
#             mi = int((st + en)/2)
#             if matrix[ind][mi] == target:
#                 return True
#             elif matrix[ind][mi] < target:
#                 st = mi + 1
#             else:
#                 en = mi - 1
#         return False
    
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         start = 0
#         end = len(matrix) - 1
#         while start <= end:
#             mid = int((start + end)/2)
#             if matrix[mid][0]  < target:
#                 for ind in range(start,mid + 1):
#                     found = self.binary_search(matrix,ind,target)
#                     if found:
#                         return found
                
#                 start = mid + 1
#             elif matrix[mid][0] > target:
#                 end = mid - 1
#             else:
#                 return True
#         return False
                        
            
        # return False
                        
            