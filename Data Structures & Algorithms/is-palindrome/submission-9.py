class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1: return True
        l, r = 0, len(s) - 1
        while l <= r:
            while not s[l].isalnum() and l < len(s):
                l += 1
            while not s[r].isalnum() and r > 0:
                r -= 1
            if s[l].lower() != s[r].lower(): return False
            l += 1
            r -= 1
        return True