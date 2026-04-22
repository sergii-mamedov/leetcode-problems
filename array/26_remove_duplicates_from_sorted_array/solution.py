"""
26. Remove duplicates from sorted array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
https://neetcode.io/problems/remove-duplicates-from-sorted-array/question
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        k = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[k] = nums[r]
                k += 1
        
        return k