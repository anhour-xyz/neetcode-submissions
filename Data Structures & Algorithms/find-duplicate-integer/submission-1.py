class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        j = 0
        for i in range(1,len(nums)):
            if nums[i] == nums[j]:
                return nums[i]
            j += 1