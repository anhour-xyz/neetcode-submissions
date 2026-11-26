class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globMax = nums[0]
        curMax = 0
        for n in nums:
            curMax = max(curMax + n, n)
            globMax = max(globMax,curMax)
        return globMax