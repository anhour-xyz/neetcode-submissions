class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = float('inf')
        cnt = 0
        for i in range(k):
            if blocks[i] == "W":
                cnt += 1
        res = min(res,cnt)

        for i in range(1,len(blocks)-k+1):
            if blocks[i-1] == "W":
                cnt -= 1
            if blocks[i+k-1] == "W":
                cnt += 1
            res = min(res,cnt)
        return res