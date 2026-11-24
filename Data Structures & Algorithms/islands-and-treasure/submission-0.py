class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = collections.deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append([r,c])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        level = 1
        visited = set()
        while q:
            n = len(q)
            for i in range(n):
                r, c = q.popleft()
                visited.add((r,c))
                for dr,dc in directions:
                    row, col = r + dr, c + dc
                    if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] == -1 :
                        continue
                    if (row,col) not in visited:
                        q.append([row,col])
                        visited.add((row,col))
                        grid[row][col] = level
            
            level += 1


