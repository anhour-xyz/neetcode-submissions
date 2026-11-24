class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        res = []
        for n in nums:
            res.append(total)
            total += n
        total = 0
        for i in range(len(nums)-1,-1,-1):
            if res[i] == total: return i
            res[i] -= total
            total += nums[i]
        return -1