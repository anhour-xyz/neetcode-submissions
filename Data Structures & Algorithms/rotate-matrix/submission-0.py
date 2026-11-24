class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        h, w = len(matrix), len(matrix[0])
        for i in range(h):
            for j in range(i+1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        for i in range(h):
            for j in range(w // 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][w-j-1]
                matrix[i][w-j-1] = temp
