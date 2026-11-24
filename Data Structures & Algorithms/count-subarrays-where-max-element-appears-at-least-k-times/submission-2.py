class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        target = max(nums)
        res = 0
        l = 0
        n = len(nums)
        map = defaultdict(int)
        for r in range(len(nums)):
            if nums[r] == target:
                map[target] += 1
            while map[target] >= k:
                res += n - r
                if nums[l] == target:
                    map[target] -= 1
                l += 1
        return res

