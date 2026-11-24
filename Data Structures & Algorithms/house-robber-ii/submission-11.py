class Solution:
    def help(self,nums):
        pre, cur = 0, 0
        for n in nums:
            pre, cur = cur, max(n + pre, cur)
        return cur

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        return max(self.help(nums[:-1]), self.help(nums[1:]))
