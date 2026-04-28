"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/description/
https://neetcode.io/problems/validate-parentheses/question

Use match hashmap, check stack size
"""

class Solution:
    def isValid(self, s: str) -> bool:

        match = {
            '}': '{',
            ']': '[',
            ')': '(',
        }

        stack = []
        for ch in s:
            if ch in match:
                if stack and stack[-1] == match[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)


        return True if not stack else False