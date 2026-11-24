class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r-1:
            mid = (l+r) // 2
            if target > nums[mid]: l = mid
            elif target < nums[mid]: r = mid
            else: return mid
        return -1
        