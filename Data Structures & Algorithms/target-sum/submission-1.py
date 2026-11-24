class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        for n in nums:
            next_dp = defaultdict(int)
            for total, cnt in dp.items():
                next_dp[total + n] += cnt
                next_dp[total - n] += cnt
            dp = next_dp
        return dp[target]