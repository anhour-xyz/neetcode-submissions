class Solution:
    def jump(self, nums: List[int]) -> int:
        r = 0
        l = 0
        res = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l,r + 1):
                farthest = max(farthest,nums[i]+i)
            r = farthest
            res += 1
            l += 1
        return res