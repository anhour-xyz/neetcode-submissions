class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1 or len(cost) == 2: return min(cost)
        dp = []
        dp.append(cost[0])
        dp.append(min(cost[0],cost[1]))
        for i in range(2, len(cost)):
            dp.append(min(cost[i-2] + dp[i-2], cost[i-1] + dp[i-1]))
        return dp[-1]