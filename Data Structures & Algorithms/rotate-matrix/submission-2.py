class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        row, col = len(matrix),len(matrix[0])
        for i in range(row):
            for j in range(i+1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        mid = col // 2
        for i in range(row):
            for j in range(mid):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][col-j-1]
                matrix[i][col-j-1] = temp
            
 