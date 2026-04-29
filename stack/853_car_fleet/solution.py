"""
853. Car fleet
https://leetcode.com/problems/car-fleet/description/
https://neetcode.io/problems/car-fleet/question

Sort the input arrays by car position in descending order
Iterate through the positions and compute the time required for each car to reach the target
If the computed time is greater than the last element in the stack, push it onto the stack as a new fleet
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pairs = sorted(zip(position, speed), reverse=True)

        stack = []
        for pos, sp in pairs:
            t = (target - pos) / sp

            if not stack or t > stack[-1]:
                stack.append(t)
        
        return len(stack)