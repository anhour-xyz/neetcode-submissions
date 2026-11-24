class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid) * len(grid[0])
        res = []
        check = set()
        for r in range(len(grid)):
            for c in range(len(grid)):
                if grid[r][c] in check:
                    res.append(grid[r][c])
                check.add(grid[r][c])

        for i in range(1,n+1):
            if i not in check:
                res.append(i)
                return res
