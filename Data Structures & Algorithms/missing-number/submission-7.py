class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)+1):
            total += i
        
        if total - sum(nums) == 0: return 0
        else: return total - sum(nums)