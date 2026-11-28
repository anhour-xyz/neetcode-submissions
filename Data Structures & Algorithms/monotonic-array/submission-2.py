class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increase = decrease = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                increase += 1
                decrease = 1
            elif nums[i] < nums[i-1]:
                decrease += 1
                increase = 1
            else:
                increase += 1
                decrease += 1

        return increase == len(nums) or decrease == len(nums)
