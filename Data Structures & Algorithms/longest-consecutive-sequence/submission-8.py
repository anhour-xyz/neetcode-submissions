class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        res = 0
        for n in check:
            if n - 1 not in check:
                length = 1
                cur = n
                while cur + 1 in check:
                    cur = cur+1
                    length += 1
                res = max(res,length)
        return res