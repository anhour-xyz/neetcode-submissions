class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1
        rows = cols = len(grid)
        q = deque()
        q.append([0,0])
        step = 0
        grid[0][0] = 1
        directions = [[-1,0],[1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,-1],[-1,1]]
        while q:
            step += 1
            for _ in range(len(q)):
                r,c = q.popleft()
                if r == rows - 1 and c == cols - 1: return step
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 0:
                        grid[row][col] = 1
                        q.append((row,col))
        return -1