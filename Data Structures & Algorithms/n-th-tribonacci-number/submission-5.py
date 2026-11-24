class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 or n == 1: return n
        if n == 2: return 1
        one,two,three = 0,1,1
        for i in range(n-2):
            temp = one + two + three
            one,two = two,three
            three = temp
        return three