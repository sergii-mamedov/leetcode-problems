"""
71. Simplify path
https://leetcode.com/problems/simplify-path/description/
https://neetcode.io/problems/simplify-path/question
"""

class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []
        for st in path.split('/'):

            if st == '' or st == '.':
                continue
            elif st == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(st)
        
        return '/' + '/'.join(stack)