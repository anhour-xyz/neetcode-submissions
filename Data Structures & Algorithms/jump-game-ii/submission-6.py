class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        step = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest, nums[i]+i)
            r = farthest
            l += 1
            step += 1
        return step