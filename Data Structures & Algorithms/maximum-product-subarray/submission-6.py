class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        f_max = f_min = 1
        res = float('-inf')
        for n in nums:
            if n < 0:
                f_max, f_min = f_min, f_max
            f_max = max(f_max * n, n)
            f_min = min(f_min * n, n)
            res = max(res,f_max)
        return res