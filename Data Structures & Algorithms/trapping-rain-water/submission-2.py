class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left_h = right_h = 0
        total = 0
        while l < r:
            left_h = max(left_h,height[l])
            right_h = max(right_h,height[r])
            if height[l] <= height[r]:
                total += left_h - height[l]
                l += 1
            else:
                total += right_h - height[r]
                r -= 1
        return total