class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 or n == 1: return n
        one, two, three = 0, 1, 1
        for _ in range(n-2):
            one, two, three = two, three, one + two + three
        return three