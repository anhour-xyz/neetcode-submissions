class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for target in range(1,n+1):
            for s in range(1,int(target **0.5)+1):
                dp[target] = min(dp[target], 1 + dp[target - s*s])
        return dp[n]
