class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        arr = set(nums)
        for n in arr:
            if n - 1 not in arr:
                length = 1
                while n + 1 in arr:
                    length += 1
                    n += 1
                res = max(res, length)
        return res