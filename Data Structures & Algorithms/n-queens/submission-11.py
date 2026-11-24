class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = set()
        diag = set()
        anti_diag = set()

        def dfs(row,board):
            if row == n:
                res.append(["".join(r) for r in board])
                return
            for col in range(n):
                if col in cols or (row-col) in diag or (row+col) in anti_diag: continue
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
        return res