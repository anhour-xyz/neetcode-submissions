class Solution:
    def totalNQueens(self, n: int) -> int:
        self.cnt = 0
        cols = set()
        diag = set()
        anti_diag = set()

        def dfs(row,board):
            if row == n:
                self.cnt += 1
                return
            for col in range(n):
                if col in cols or (row-col) in diag or (row+col) in anti_diag: 
                    continue
                cols.add(col)
                diag.add(row-col)
                anti_diag.add(row+col)
                board[row][col] = "Q"
                dfs(row+1,board)
                board[row][col] = "."
                cols.remove(col)
                diag.remove(row-col)
                anti_diag.remove(row+col)
        board = [["." for _ in range(n)] for _ in range(n)]
        dfs(0,board)
        return self.cnt 