"""
1768. Merge strings alternately
https://leetcode.com/problems/merge-strings-alternately/description/
https://neetcode.io/problems/merge-strings-alternately/question

Tip: Use array for result and join later
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        lenght1 = len(word1)
        lenght2 = len(word2)

        result = []
        for i in range(max(lenght1, lenght2)):
            if i < lenght1:
                result.append(word1[i])
            if i < lenght2:
                result.append(word2[i])
        
        return ''.join(result)