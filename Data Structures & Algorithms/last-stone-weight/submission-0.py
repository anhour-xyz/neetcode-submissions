class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1: return stones[0]

        if stones[0] != stones[1]:
            res = abs(stones[0] - stones[1])
        else:
            res = 0

        for i in range(2, len(stones)):
            if stones[i] < res:
                res = res - stones[i]
            elif stones[i] > res:
                res = stones[i] - res
            else: res = 0
        return res
