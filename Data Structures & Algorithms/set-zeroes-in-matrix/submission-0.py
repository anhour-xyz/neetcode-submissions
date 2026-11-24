class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = defaultdict(int)
        col = defaultdict(int)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] += 1
                    col[j] += 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row:
                    matrix[i][j] = 0
                if j in col:
                    matrix[i][j] = 0
                    
        