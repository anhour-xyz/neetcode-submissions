class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        check = set(nums)
        for n in check:
            if n-1 not in check:
                length = 1
                while n + 1 in check:
                    n += 1
                    length += 1
                res = max(length, res)
        return res