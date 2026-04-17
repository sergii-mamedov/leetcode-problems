"""
1. Two Sum
https://leetcode.com/problems/two-sum/description/
https://neetcode.io/problems/two-integer-sum/question

neetcode asks to return indexes sorted
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        for i, num in enumerate(nums):
            val = target - num
            if val in seen:
                return [i, seen[val]]
            else:
                seen[num] = i