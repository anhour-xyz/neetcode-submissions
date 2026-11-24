class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        res = float('-inf')

        for n in nums:
            total = max(total + n, n)
            res = max(res,total)
        return res