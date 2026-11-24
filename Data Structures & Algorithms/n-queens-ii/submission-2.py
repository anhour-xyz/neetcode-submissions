class Solution:
    def totalNQueens(self, n: int) -> int:
        
        self.cnt = 0
        cols,diag,anti_diag = set(),set(),set()
        def dfs(row):
            if row == n:
                self.cnt += 1
                return 
            for col in range(n):
                if col in cols or row - col in diag or row + col in anti_diag:
                    continue
                cols.add(col)
                diag.add(row-col)
                anti_diag.add(row+col)
                dfs(row+1)
                cols.remove(col)
                diag.remove(row-col)
                anti_diag.remove(row+col)
        dfs(0)
        return self.cnt

