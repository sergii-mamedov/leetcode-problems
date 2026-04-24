"""
15. 3Sum
https://leetcode.com/problems/3sum/description/
https://neetcode.io/problems/three-integer-sum/question

After sorting the array, fix one element i and use two pointers L and R to find a pair, 
moving them based on the current sum. When a valid triplet is found, immediately store it, 
move both pointers inward, and then skip duplicate values to avoid repeating results. 
Should not use break after the first match.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            L, R = i+1, len(nums) - 1
            while L < R:
                s = nums[i] + nums[L] + nums[R]

                if s > 0:
                    R -= 1
                elif s < 0:
                    L += 1
                else:
                    result.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1

                    while L < R and nums[L] == nums[L-1]:
                        L += 1
                    
                    while L < R and nums[R] == nums[R+1]:
                        R -= 1

        return result