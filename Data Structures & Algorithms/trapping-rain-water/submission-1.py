class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = left_suf=right_suf=0
        while l < r:
            left_suf = max(left_suf, height[l])
            right_suf = max(right_suf,height[r])
            if height[l] <= height[r]:
                res += left_suf - height[l]
                l += 1
            else:
                res += right_suf - height[r]
                r -= 1
        return res