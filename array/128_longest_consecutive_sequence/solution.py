"""
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/description/
https://neetcode.io/problems/longest-consecutive-sequence/question

Use a set to achieve O(1) lookups for checking whether a number exists.
Only start building sequences from numbers that don’t have a predecessor (num - 1), 
since those are the only valid starting points.
From each such number, expand the sequence forward (num + 1, num + 2, ...) 
as long as the elements exist in the set.
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        longest = 0
        nums = set(nums)
        for i in nums:
            if (i-1) not in nums:
                lenght = 1
                current = i

                while (current+1) in nums:
                    lenght += 1
                    current += 1
            
                longest = max(longest, lenght)
        
        return longest