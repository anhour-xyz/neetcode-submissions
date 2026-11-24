class Solution:
    def climbStairs(self, n: int) -> int:
        one,second = 1,1
        for i in range(2,n+1):
            temp = one
            one = one + second
            second = temp
        return one
