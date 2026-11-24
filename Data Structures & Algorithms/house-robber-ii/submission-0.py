class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1 or len(nums) == 2: return max(nums)
        dp = []
        dp.append(nums[0])
        dp.append(max(nums[0],nums[1]))
        dp.append(max(dp[-1], nums[2]))
        for i in range(3, len(nums)):
            dp.append(max(dp[i-1], nums[i] + dp[i-2]))
        return dp[-1]