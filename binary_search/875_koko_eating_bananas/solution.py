"""
875. Koko eating banannas
https://leetcode.com/problems/koko-eating-bananas/description/
https://neetcode.io/problems/eating-bananas/question

Binary search, where l = 1 and r = max(pilis).
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        result = r
        while l <= r:

            total_time = 0
            k = l + (r - l) // 2

            for pile in piles:
                total_time += (pile + k - 1 ) // k
            
            if total_time <= h:
                result = k
                r = k - 1
            else:
                l = k + 1
        
        return result