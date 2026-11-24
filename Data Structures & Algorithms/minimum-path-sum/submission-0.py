class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = grid
        rows, cols = len(grid), len(grid[0])
        for c in range(1,cols):
            dp[0][c] = grid[0][c] + dp[0][c-1]
        for r in range(1,rows):
            dp[r][0] = grid[r][0] + dp[r-1][0]

        for r in range(1,rows):
            for c in range(1,cols):
                dp[r][c] = min(grid[r][c] + dp[r-1][c], grid[r][c] + dp[r][c-1])
        return dp[-1][-1]
