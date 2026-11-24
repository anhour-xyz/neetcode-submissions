class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        rows, cols = len(matrix), len(matrix[0])
        s = [[0] * (cols+1) for _ in range(rows+1)]
        for i, row in enumerate(matrix):
            for j, n in enumerate(row):
                s[i+1][j+1] = s[i+1][j] + s[i][j+1] - s[i][j] + n

        self.s = s
    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        s = self.s
        return s[r2+1][c2+1] - s[r2+1][c1] - s[r1][c2+1] + s[r1][c1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)