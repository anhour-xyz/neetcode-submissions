class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        minHeap = [[grid[0][0],0,0]]
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        while minHeap:
            w, r, c = heapq.heappop(minHeap)
            if r == rows - 1 and c == cols - 1: return w
            if (r,c) in visit: continue
            visit.add((r,c))
            for dr, dc in directions:
                row, col = r + dr, c + dc 
                if 0 <= row < rows and 0 <= col < cols and (row,col) not in visit:
                    heapq.heappush(minHeap,[max(w,grid[row][col]),row,col])