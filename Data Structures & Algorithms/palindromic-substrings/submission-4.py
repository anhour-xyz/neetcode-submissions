class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)):
            l = r = i
            cnt += self.count(s,l,r)
            
            l,r = i, i+1
            cnt += self.count(s,l,r)
        return cnt

    def count(self,s,l,r):
        cnt = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1
        return cnt