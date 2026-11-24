class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cnt = 0
        res = 0
        for i in range(k):
            if s[i] in 'aeiou':
                cnt += 1
        res = max(res,cnt)
        for i in range(1,len(s)-k+1):
            if s[i-1] in 'aeiou':
                cnt -= 1
            if s[i+k-1] in 'aeiou':
                cnt += 1
            res = max(res,cnt)
        return res