class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        total = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                total += nums[i]
            else:
                total = nums[i]
            res = max(res,total)
        return res
