"""
238. Product of array except self
https://leetcode.com/problems/product-of-array-except-self/description/
https://neetcode.io/problems/products-of-array-discluding-self/question
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        left = [1] * n
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        
        right = [1] * n
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        
        result = [1] * n
        for i in range(n):
            result[i] = left[i] * right[i]
        
        return result