class Solution:
    def rob(self, nums: List[int]) -> int:
        pre = cur = 0
        for n in nums:
            pre, cur = cur, max(pre + n, cur)
        return cur