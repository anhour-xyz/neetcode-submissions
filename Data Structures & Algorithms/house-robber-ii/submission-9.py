class Solution:


    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        return max(self.help(nums[:-1]), self.help(nums[1:]))
    
    def help(self,nums):
        cur = pre = 0
        for n in nums:
            cur,pre = max(n+pre, cur), cur
        return cur

        