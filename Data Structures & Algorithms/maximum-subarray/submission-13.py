class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curTotal = 0
        res = max(nums)
        for n in nums:
            curTotal = max(curTotal+n, n)
            res = max(res,curTotal)
        return res