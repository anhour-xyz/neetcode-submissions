class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        res = []
        atl, pac = set(), set()
        def dfs(r,c,preHeight,ocean):
            if r < 0 or c < 0 or r >= rows or c >= cols or heights[r][c] < preHeight or (r,c) in ocean:
                return
            ocean.add((r,c))
            dfs(r+1,c,heights[r][c],ocean)
            dfs(r-1,c,heights[r][c],ocean)
            dfs(r,c+1,heights[r][c],ocean)
            dfs(r,c-1,heights[r][c],ocean)

        for r in range(rows):
            dfs(r,0,heights[r][0],pac)
            dfs(r,cols-1,heights[r][cols-1],atl)
        
        for c in range(cols):
            dfs(0,c,heights[0][c], pac)
            dfs(rows-1,c,heights[rows-1][c], atl)

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res