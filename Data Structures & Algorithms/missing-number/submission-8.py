class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        target = total = 0
        for i in range(0,len(nums)+1):
            target += i

        for n in nums:
            total += n

        if total == target: return 0
        else: return target - total

        