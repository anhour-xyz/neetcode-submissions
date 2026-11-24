class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1 for _ in range(cols)] for _ in range(rows)]
        for c in range(cols):
            if obstacleGrid[0][c] == 1:
                for i in range(c,cols):
                    dp[0][i] = 0
        for r in range(rows):
            if obstacleGrid[r][0] == 1:
                for i in range(r,rows):
                    dp[i][0] = 0

        for r in range(1,rows):
            for c in range(1,cols):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[-1][-1]