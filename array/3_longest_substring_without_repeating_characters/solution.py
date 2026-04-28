"""
3. Longest substing without repeating characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
https://neetcode.io/problems/longest-substring-without-duplicates/question

use hashmap for seen. Use while loop to remove old characters
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()

        l = 0
        size = 0
        for r in range(len(s)):

            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            size = max(size, r - l + 1)
        
        return size