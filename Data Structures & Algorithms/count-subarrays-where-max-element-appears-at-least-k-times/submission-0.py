class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        target = max(nums)
        l = 0
        cnt = 0
        res = 0
        n = len(nums)
        for r in range(len(nums)):
            if nums[r] == target:
                cnt += 1
            while cnt >= k:
                res += n - r 
                if nums[l] == target: cnt -= 1
                l += 1
        return res