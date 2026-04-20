"""
238. Product of array except self
https://leetcode.com/problems/product-of-array-except-self/description/
https://neetcode.io/problems/products-of-array-discluding-self/question

Only ONE additional array.
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        result = [1] * n

        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result