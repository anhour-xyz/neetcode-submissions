class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        r = len(s) - 1
        while r >= 0:
            while r >= 0 and not s[r].isalnum():
                r -= 1
            while r >= 0 and s[r].isalnum():
                r -= 1
                length += 1
            return length