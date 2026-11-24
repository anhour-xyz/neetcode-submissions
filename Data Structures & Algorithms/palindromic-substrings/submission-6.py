class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        def help(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                nonlocal cnt
                cnt += 1
                l -= 1
                r += 1

        for i in range(len(s)):
            l = r = i
            help(l,r)
            l, r = i, i + 1
            help(l,r)
            
        return cnt