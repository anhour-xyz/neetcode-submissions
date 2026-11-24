class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        res = 0
        for n in nums:
            if n == 1:
                cnt += 1
                res = max(res,cnt)
            else:
                cnt = 0
        return res
