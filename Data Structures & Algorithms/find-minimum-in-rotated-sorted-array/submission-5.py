class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if len(nums) == 1: return nums[0]
        if nums[l] < nums[r]:
            return nums[l]
        else:
            while l < r:
                mid = (l+r) // 2
                if nums[r] < nums[r-1] and nums[r] < nums[l]: return nums[r]
                elif nums[mid] < nums[mid+1] and nums[mid] < nums[mid-1]:
                    return nums[mid]
                elif nums[mid] > nums[l] and nums[mid] > nums[r]: l = mid
                elif nums[mid] < nums[r]: r = mid