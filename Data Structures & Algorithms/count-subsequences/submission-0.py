class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        check = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
        for j in range(len(s)+1):
            check[j][len(t)] = 1
        for i in range(len(s)-1,-1,-1):
            for j in range(len(t)-1,-1,-1):
                check[i][j] = check[i+1][j]
                if t[j] == s[i]:
                    check[i][j] += check[i+1][j+1]
        return check[0][0]
