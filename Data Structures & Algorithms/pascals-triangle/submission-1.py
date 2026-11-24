class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1]]
        for i in range(1,numRows):
            temp = []
            for j in range(i+1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(dp[i-1][j] + dp[i-1][j-1])
            dp.append(temp)
        return dp