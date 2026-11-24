class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = defaultdict(list), defaultdict(list), defaultdict(list)

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".": continue
                if num in rows[r] or num in cols[c] or num in squares[(r//3, c//3)]:
                    return False
                rows[r].append(num)
                cols[c].append(num)
                squares[(r//c,c//3)].append(num)

        return True