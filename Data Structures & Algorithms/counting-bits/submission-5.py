class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            temp = 0
            for j in range(32):
                if i & (1 << j):
                    temp += 1
            res.append(temp)
        return res