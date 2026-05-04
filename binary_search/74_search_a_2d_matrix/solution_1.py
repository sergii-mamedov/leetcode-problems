"""
74. Search a 2D matrix
https://leetcode.com/problems/search-a-2d-matrix/description/
https://neetcode.io/problems/search-2d-matrix/question

2D solution
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row_id = None
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = l + (r-l) // 2

            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else:
                row_id = m
                break
        
        if row_id is None:
            return False
        
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = l + (r - l) // 2

            if target == matrix[row_id][m]:
                return True
            elif target > matrix[row_id][m]:
                l = m + 1
            else:
                r = m - 1
        
        return False