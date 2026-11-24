class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self,nums:List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1 or len(nums) == 2: return max(nums)
        dp = []
        dp.append(nums[0])
        dp.append(max(nums[0],nums[1]))

        for i in range(2, len(nums)):
            dp.append(max(dp[i-1], nums[i] + dp[i-2]))
        return dp[-1]
        