class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        dp = []
        dp.append(nums[0])
        for i in range(1, len(nums)):
            dp.append(max(max(nums[i], dp[i-1]*nums[i]),nums[i-1] * nums[i]))
        return max(dp)