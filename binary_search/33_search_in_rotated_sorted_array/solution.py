"""
33. Search in rotated sorted array
https://leetcode.com/problems/search-in-rotated-sorted-array/description/
https://neetcode.io/problems/find-target-in-rotated-sorted-array/question

If-else for the left/right side. Check the target between pointers.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m

            # left is sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # right is sorted
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        
        return -1