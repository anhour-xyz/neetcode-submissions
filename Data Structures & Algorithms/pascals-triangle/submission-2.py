class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for r in range(1,numRows):
            temp = []
            for c in range(r+1):
                if c == 0 or c == r:
                    temp.append(1)
                else:
                    temp.append(res[r-1][c] + res[r-1][c-1])
            res.append(temp)
        return res