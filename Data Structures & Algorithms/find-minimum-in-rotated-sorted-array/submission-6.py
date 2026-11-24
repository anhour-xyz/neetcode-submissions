class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        if len(nums) == 1: return nums[0]
        if nums[l] < nums[r]: return nums[l]
        elif nums[l] > nums[r] and nums[r] < nums[r-1]: return nums[r]
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] < nums[mid+1] and nums[mid] < nums[mid-1]: return nums[mid]
            elif nums[mid] >= nums[l]: l = mid + 1
            else: r = mid - 1
        
