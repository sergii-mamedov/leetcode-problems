"""
189. Rotate array
https://leetcode.com/problems/rotate-array/description/
https://neetcode.io/problems/rotate-array/question

Implement a reverse function. 
Then call it sequentially: 
 - first on the entire array
 - then on the first k elements
 - finally on the remaining elements.
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(data: List[int], l: int, r: int) -> List[int]:
            while l < r:
                data[l], data[r] = data[r], data[l]
                l += 1
                r -= 1
            
        
        k = k % len(nums)
        n = len(nums)
        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)

        return None