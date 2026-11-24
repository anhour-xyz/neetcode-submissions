class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        cnt = 0
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            elif cnt < 1:
                if s[r-1] == s[l]:
                    r -= 1
                    cnt += 1
                elif s[l+1] == s[r]: 
                    l +=1
                    cnt += 1
                else: return False
            else: return False
        return True