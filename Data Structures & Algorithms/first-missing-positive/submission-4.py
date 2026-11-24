class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(len(nums)):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i]-1]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        for i, n in enumerate(nums):
            if n != i + 1: return i + 1
        return n