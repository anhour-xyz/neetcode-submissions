class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[1 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        for c in range(cols):
            if obstacleGrid[0][c] == 1:
                for i in range(c,cols):
                    dp[0][i] = 0
                break
        for r in range(rows):
            if obstacleGrid[r][0] == 1:
                for j in range(r,rows):
                    dp[r][0] = 0
                break
        
        for r in range(1,rows):
            for c in range(1,cols):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[-1][-1]