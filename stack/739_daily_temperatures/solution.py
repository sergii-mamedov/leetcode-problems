"""
739. Daily temperature
https://leetcode.com/problems/daily-temperatures/description/
https://neetcode.io/problems/daily-temperatures/question

A stack of indices is maintained for days for which the next warmer day has not yet been found.
For each new day, its temp is compared with the temp at the top of the stack.
While the current temp is higher, indices are popped from the stack and 
the difference in indices is recorded in the result array.
After that, the current day is pushed onto the stack as a new candidate.
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):

            while stack and t > temperatures[stack[-1]]:
                idx = stack[-1]
                result[idx] = i - idx
                stack.pop()

            stack.append(i)
        
        return result