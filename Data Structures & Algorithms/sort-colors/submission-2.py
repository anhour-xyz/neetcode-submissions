class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt0 = cnt1 = 0
        for i, n in enumerate(nums):
            nums[i] = 2
            if n <= 1:
                nums[cnt1] = 1
                cnt1 += 1
            if n == 0:
                nums[cnt0] = 0
                cnt0 += 1
            