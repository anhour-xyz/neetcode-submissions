class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        longest = 0
        for i in check:
            if i-1 not in check:
                length = 1
                cur = i
                while cur + 1 in check:
                    length += 1
                    cur += 1
                longest = max(longest,length)
        return longest