"""
680. Valid palindrome II
https://leetcode.com/problems/valid-palindrome-ii/description/
https://neetcode.io/problems/valid-palindrome-ii/question

If the values for L,R pointers do not match, need to run is_palindrome for the 
pairs (L+1, R) and (L, R-1)
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_palindrome(l: int, r: int):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        L, R = 0, len(s) - 1

        while L < R:
            if s[L] != s[R]:
                return is_palindrome(L+1, R) or is_palindrome(L, R-1)

            L += 1
            R -= 1

        return True