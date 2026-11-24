class Solution:
    def totalNQueens(self, n: int) -> int:
        cols, diag, anti_diag = set(), set(), set()
        res = 0

        def dfs(row):
            nonlocal res
            if row == n:
                res += 1
                return
            for col in range(n):
                if col in cols or (row-col) in diag or (row +col) in anti_diag:
                    continue
                cols.add(col)
                diag.add(row-col)
                anti_diag.add(row+col)
                dfs(row+1)
                cols.remove(col)
                diag.remove(row-col)
                anti_diag.remove(row+col)
        
        dfs(0)
        return res
