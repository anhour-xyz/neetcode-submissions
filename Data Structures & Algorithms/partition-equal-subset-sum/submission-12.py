class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0: return False
        target = sum(nums) // 2
        dp = [False] * (target+1)
        dp[0] = True
        for n in nums:
            for a in range(target,0,-1):
                if a >= n:
                    dp[a] = dp[a] or dp[a-n]
        return dp[target]