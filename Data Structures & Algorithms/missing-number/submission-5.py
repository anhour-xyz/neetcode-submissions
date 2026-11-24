class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        if len(nums) != max(nums): return len(nums)
        for i in range(len(nums)+1):
            total += i
        check = 0
        for n in nums:
            check += n   
        if total == check: return 0
        else: return total - check