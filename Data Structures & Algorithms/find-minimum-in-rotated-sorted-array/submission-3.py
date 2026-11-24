class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return min(nums)
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            if mid == 0 and nums[mid] < nums[mid+1]: return nums[mid]
            elif mid == len(nums) - 1 and nums[mid] < nums[mid-1] :
                return nums[mid]
            elif nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]: return nums[mid]
            elif nums[mid] > nums[mid-1] and nums[mid] > nums[r]: l = mid+1
            elif nums[mid] > nums[mid-1] and nums[mid] < nums[r]: r = mid-1

