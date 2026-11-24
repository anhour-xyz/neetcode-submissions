class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visit = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visit.add((r,c))
                    q.append([r,c])
        level = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            level += 1
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    row,col = r+dr,c+dc
                    if row < 0 or col < 0 or row >= rows or col >= cols or (row,col) in visit or grid[row][col] == -1:
                        continue
                    q.append([row,col])
                    grid[row][col] = level
                    visit.add((row,col))
        
