class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        length = 0
        check = set()
        for r in range(len(s)):
            while s[r] in check:
                check.remove(s[l])
                l +=1
            check.add(s[r])
            length = max(length,r-l+1)
        return length