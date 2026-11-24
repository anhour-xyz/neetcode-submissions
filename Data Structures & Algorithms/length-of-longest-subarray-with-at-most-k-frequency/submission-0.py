class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 0
        l = 0
        map = defaultdict(int)
        for r in range(len(nums)):
            map[nums[r]] += 1
            while map[nums[r]] > k:
                map[nums[l]] -= 1
                if map[nums[l]] == 0: del map[nums[l]]
                l += 1
            res = max(res, r-l+1)
        return res