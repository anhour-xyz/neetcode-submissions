class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        minHeap = [[0,heights[0][0],0,0]]
        visit = set()
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        while minHeap:
            diff, n, r, c = heapq.heappop(minHeap)
            if (r,c) in visit: continue
            visit.add((r,c))
            if r == rows - 1 and c == cols - 1: return diff
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if 0 <= row < rows and 0 <= col < cols and (row,col) not in visit:
                    heapq.heappush(minHeap, [max(diff, abs(heights[row][col] - n)), heights[row][col], row, col])