class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t): return 0
        dp = [1] + [0] * len(t)
        for i in range(len(s)):
            for j in range(min(i,len(t)-1), max(len(t)-len(s)+i,0)-1,-1):
                if s[i] == t[j]:
                    dp[j+1] += dp[j]
        return dp[len(t)]