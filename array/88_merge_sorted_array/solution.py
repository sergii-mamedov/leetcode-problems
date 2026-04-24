"""
88. Merge sorted array
https://leetcode.com/problems/merge-sorted-array/description/

Move from the end of nums1, using two pointers (p1 for nums1, p2 for nums2), 
and at each step place the larger element at the end.
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p1, p2 = m-1, n-1
        for i in range(n+m-1, -1, -1):

            if p2 < 0:
                break
            
            if p1 >=0 and nums1[p1] >= nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
        
        return None