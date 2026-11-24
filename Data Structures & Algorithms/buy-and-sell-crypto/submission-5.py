class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfit = float('-inf')
        for p in prices:
            minPrice = min(p, minPrice)
            maxProfit = max(p-minPrice, maxProfit)
        return maxProfit