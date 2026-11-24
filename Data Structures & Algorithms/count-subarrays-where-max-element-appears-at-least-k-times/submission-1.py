class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        target = max(nums)
        map = defaultdict(int)
        n = len(nums)
        res = 0
        l = 0
        for r in range(len(nums)):
            map[nums[r]] += 1
            while map[target] >= k:
                res += n - r
                map[nums[l]] -= 1
                l += 1
        return res
