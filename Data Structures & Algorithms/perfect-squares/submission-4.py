class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for a in range(1,n+1):
            for j in range(int(a**0.5)+1):
                dp[a] = min(dp[a],1+dp[a-j*j])
        return dp[n]