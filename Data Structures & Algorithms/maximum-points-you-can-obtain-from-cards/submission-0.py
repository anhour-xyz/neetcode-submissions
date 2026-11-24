class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints) - k
        total = 0
        res = float('inf')
        for i in range(n):
            total += cardPoints[i]
        res = min(res, total)
        length =len(cardPoints)
        for i in range(1,length-n+1):
            total -= cardPoints[i-1]
            total += cardPoints[i+n-1]
            res = min(res,total)
        return sum(cardPoints) - res
