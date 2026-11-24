class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(arr):
            l, r = 0, len(arr) - 1
            while l < r:
                if arr[l] != arr[r]: return False
                l += 1
                r -= 1
            return True
        
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]: return check(s[l+1:r+1]) or check(s[l:r])
            l += 1
            r -= 1
        return True