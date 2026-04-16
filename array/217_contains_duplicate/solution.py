"""
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/description/
https://neetcode.io/problems/duplicate-integer/question
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)

        return False
