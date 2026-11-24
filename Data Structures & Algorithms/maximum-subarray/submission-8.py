class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1,len(nums)):
            res = max(res + nums[i], nums[i])
        return res
