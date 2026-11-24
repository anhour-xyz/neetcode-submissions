class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        minHeap = [[grid[0][0],0,0]]

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visit.add((0,0))

        while minHeap:
            t,r,c = heapq.heappop(minHeap)

            if r == n-1 and c == n - 1: return t
            for dr,dc in directions:
                row,col = r + dr, c + dc
                if row < 0 or col < 0 or row >= n or col >= n or (row,col) in visit:
                    continue
                visit.add((row,col))
                heapq.heappush(minHeap,[max(t,grid[row][col]),row,col])
        