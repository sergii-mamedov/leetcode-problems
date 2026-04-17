"""
169. Majority element
https://leetcode.com/problems/majority-element/description/
https://neetcode.io/problems/majority-element/question
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        seen = {}
        for n in nums:
            seen[n] = seen.get(n, 0) + 1
        
        count = 0
        for k,v in seen.items():
            if v > count:
                count = v
                major_element = k
        
        return major_element