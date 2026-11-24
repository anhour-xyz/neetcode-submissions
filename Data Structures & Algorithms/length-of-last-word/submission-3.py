class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = len(s) - 1
        while r >= 0 and not s[r].isalnum():
            r -= 1
        
        cnt = 0
        while r >= 0 and s[r].isalnum():
            r -= 1
            cnt += 1
        return cnt