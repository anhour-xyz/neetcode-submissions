class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 0
        map = defaultdict(int)
        l = 0
        for r in range(len(nums)):
            map[nums[r]] += 1
            while map[nums[r]] > k:
                map[nums[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res