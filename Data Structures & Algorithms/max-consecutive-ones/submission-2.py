class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt_1 = 0
        res = 0
        for n in nums:
            if n == 1:
                cnt_1 += 1
                res = max(res,cnt_1)
            else:
                cnt_1 = 0

        return res