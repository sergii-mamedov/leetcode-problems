"""
150. Evaluate reverse polish notation
https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
https://neetcode.io/problems/evaluate-reverse-polish-notation/question

Two times pop()
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for ch in tokens:
            if ch == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif ch == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif ch == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif ch == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(ch))
        
        return stack[0]