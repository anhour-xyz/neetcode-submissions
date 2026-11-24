class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                while stack and abs(a) >= stack[-1]:
                    if abs(a) == stack[-1]:
                        stack.pop()
                    else:
                        n = stack.pop()
                        stack.append(abs(a) - n)
                        if len(stack) == 1: break
        return stack