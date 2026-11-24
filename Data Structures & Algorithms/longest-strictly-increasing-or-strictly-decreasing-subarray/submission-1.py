class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        decrease = increase = 1
        cnt_increase = cnt_decrease = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                cnt_increase += 1
                increase = max(increase,cnt_increase)
                cnt_decrease = 1
            elif nums[i] < nums[i-1]:
                cnt_decrease += 1
                decrease = max(decrease,cnt_decrease)
                cnt_increase = 1
            else:
                cnt_decrease = 1
                cnt_increase = 1

        return max(increase,decrease)
        