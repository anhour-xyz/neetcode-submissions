class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                temp = abs(a)
                while stack and temp >= stack[-1]:
                    if abs(a) == stack[-1]:
                        stack.pop()
                    else:
                        n = stack.pop()
                        temp = abs(a) - n
                        if len(stack) == 0: 
                            stack.append(temp)
                            break
        return stack