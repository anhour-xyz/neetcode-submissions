class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        target = 0
        total = 0
        for n in nums:
            total += n
        for i in range(len(nums)+1):
            target += i
        
        if target == total: return 0
        else: return target - total