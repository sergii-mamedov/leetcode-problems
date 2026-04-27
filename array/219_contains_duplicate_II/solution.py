"""
219. Contains duplicate II
https://leetcode.com/problems/contains-duplicate-ii/description/
https://neetcode.io/problems/contains-duplicate-ii/question

Use set-based window for checking values.
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        window = set()

        l = 0
        for r in range(len(nums)):
            if nums[r] in window:
                return True
            
            window.add(nums[r])

            if (r-l) >= k:
                window.remove(nums[l])
                l += 1
        
        return False