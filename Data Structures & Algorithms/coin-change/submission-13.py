class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for a in range(amount+1):
            for n in coins:
                if a >= n:
                    dp[a] = min(dp[a], 1+dp[a-n])
        return dp[amount] if dp[amount] != float('inf') else -1