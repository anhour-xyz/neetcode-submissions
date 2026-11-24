class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r,c):
            q = deque()
            q.append([r,c])
            directions = [[-1,0], [1,0], [0,1],[0,-1]]
            while q:
                for _ in range(len(q)):
                    r,c = q.popleft()
                    for dr, dc in directions:
                        row,col = r + dr, c + dc
                        if 0 <= row < rows and 0 <= col < cols and grid[row][col] == "1":
                            grid[row][col] = '0'
                            q.append([row,col])


            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
        return islands