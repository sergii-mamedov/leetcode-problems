"""
69. Sqrt(x)
https://leetcode.com/problems/sqrtx/description/
https://neetcode.io/problems/sqrtx/question

Return right pointer
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        
        l, r = 0, x
        while l <= r:
            m = l + (r-l) // 2
            m2 = m * m
            
            if m2 == x:
                return m
            elif m2 > x:
                r = m - 1
            else:
                l = m + 1
        
        return r