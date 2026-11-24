class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        total = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                total += nums[i]
                res = max(total,res)
            else:
                total = nums[i]
        return res
