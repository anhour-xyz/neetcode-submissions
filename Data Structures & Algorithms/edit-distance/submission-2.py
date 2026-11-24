class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float('inf') for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

        for c in range(len(dp[0])):
            dp[len(dp)-1][c] = len(word2) - c
        
        for r in range(len(dp)):
            dp[r][len(dp[0])-1] = len(word1) - r

        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])
        return dp[0][0]