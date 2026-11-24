class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1]]
        for r in range(1,rowIndex+1):
            temp = []
            for i in range(r+1):
                if i == 0 or i == r:
                    temp.append(1)
                else:
                    temp.append(dp[r-1][i-1] + dp[r-1][i])
            dp.append(temp)
        return dp[-1]