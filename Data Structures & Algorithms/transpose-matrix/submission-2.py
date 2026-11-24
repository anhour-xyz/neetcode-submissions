class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [[1 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

        for c in range(len(matrix[0])):
            for r in range(len(matrix)):
                res[c][r] = matrix[r][c]
        return res
