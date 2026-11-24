class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diag = set()
        anti_diag = set()
        res = []
        def dfs(row, board):
            if row == n:
                res.append([''.join(row) for row in board])
                return 

            for col in range(n):
                if col in cols or col + row in anti_diag or row - col in diag:
                    continue
                cols.add(col)
                diag.add(row-col)
                anti_diag.add(row+col)
                board[row][col] = "Q"
                dfs(row+1,board)
                cols.remove(col)
                diag.remove(row-col)
                anti_diag.remove(row+col)
                board[row][col] = "."
        board = [["." for _ in range(n)] for _ in range(n)]
        dfs(0,board)
        return res