class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0:
            while i >= 0 and not s[i].isalnum():
                i -= 1
            cnt = 0
            while i >= 0 and s[i].isalnum():
                i -= 1
                cnt += 1
            return cnt