"""
347. Top K frequent element
https://leetcode.com/problems/top-k-frequent-elements/description/
https://neetcode.io/problems/top-k-elements-in-list/question

Tip: use bucket sort
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, fr in freq.items():
            buckets[fr].append(num)

        result = []
        for fr in range(len(nums), 0, -1):
            for num in buckets[fr]:
                result.append(num)
                if len(result) == k:
                    return result