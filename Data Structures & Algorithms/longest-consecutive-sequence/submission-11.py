class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        for n in nums:
            if n-1 not in nums:
                length = 1
                while n+1 in nums:
                    n += 1
                    length += 1
                res = max(res,length)
        return res