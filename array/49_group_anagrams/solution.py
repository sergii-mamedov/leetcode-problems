"""
49. Group anagrams
https://leetcode.com/problems/group-anagrams/description/
https://neetcode.io/problems/anagram-groups/question
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        results = {}
        for string in strs:
            s = ''.join(sorted(string))
            if s in results:
                results[s].append(string)
            else:
                results[s] = [string]
        
        return list(results.values())