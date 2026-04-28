"""
735. Asteroid collision
https://leetcode.com/problems/asteroid-collision/description/
https://neetcode.io/problems/asteroid-collision/question

Use alive, check stack, check direction last in stack and current
"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        for a in asteroids:

            alive = True
            while alive and stack and stack[-1] > 0 and a < 0:
                if abs(stack[-1]) > abs(a):
                    alive = False
                elif abs(stack[-1]) < abs(a):
                    stack.pop()
                else:
                    stack.pop()
                    alive = False

            if alive:
                stack.append(a)
        
        return stack