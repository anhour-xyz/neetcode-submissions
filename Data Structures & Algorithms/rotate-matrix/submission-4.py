class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            for c in range(r+1):
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp

        mid = cols // 2
        for r in range(rows):
            for c in range(mid):
                temp = matrix[r][c]
                matrix[r][c] = matrix[r][cols-c-1]
                matrix[r][cols-c-1] = temp
        