class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 0, 1
        for i in range(n):
            temp = one
            one = two
            two += temp
        return two

