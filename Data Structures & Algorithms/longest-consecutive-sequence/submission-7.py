class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        longest = 0
        for n in check:
            if n - 1 not in check:
                length = 1
                cur = n
                while cur + 1 in check:
                    length += 1
                    cur += 1
                longest = max(longest, length)
        return longest