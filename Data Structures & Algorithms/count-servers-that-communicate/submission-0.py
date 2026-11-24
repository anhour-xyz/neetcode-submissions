class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row, col = defaultdict(int), defaultdict(int)
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row[r] += 1
                    col[c] += 1
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if row[r] > 1 or col[c] > 1:
                        res += 1
        return res