class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin = float('inf')
        curMax = float('-inf')
        res = float('-inf')
        for n in nums:
            if n < 0:
                curMin, curMax = curMax, curMin
            curMin = min(curMin * n, n)
            curMax = max(curMax * n, n)
            res = max(res, curMax)
        return res