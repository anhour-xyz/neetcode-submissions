class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = left = right = 0
        while l < r:
            left = max(left, height[l])
            right = max(right, height[r])
            if height[l] <= height[r]:
                res += left - height[l]
                l += 1
            else:
                res += right - height[r]
                r -= 1
        return res