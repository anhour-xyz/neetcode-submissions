class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        res = float('inf')
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                total -= nums[l]
                res = min(res,r-l+1)
                l += 1
            
        return res if res != float('inf') else 0
