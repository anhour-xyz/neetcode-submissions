class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        res = -1 
        l = 0
        total = 0
        for r in range(len(nums)):
            total += nums[r]
            while total > target:
                total -= nums[l]
                l += 1
            if total == target:
                res = max(res,r-l+1)
        return len(nums) - res if res != -1 else -1