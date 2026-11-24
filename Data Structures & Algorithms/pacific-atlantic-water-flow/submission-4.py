class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        res = []
        pac, atl = set(), set()

        def dfs(r,c,ocean,preVal):
            if r < 0 or c < 0 or r >= rows or c >= cols or heights[r][c] < preVal or (r,c) in ocean:
                return
            ocean.add((r,c))
            dfs(r+1,c,ocean,heights[r][c])
            dfs(r-1,c,ocean,heights[r][c])
            dfs(r,c+1,ocean,heights[r][c])
            dfs(r,c-1,ocean,heights[r][c])

        for r in range(rows):
            dfs(r,0,pac,-1)
            dfs(r,cols-1,atl,-1)
        
        for c in range(cols):
            dfs(0,c,pac,-1)
            dfs(rows-1,c,atl,-1)

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res