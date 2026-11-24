class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        profit = float('-inf')
        minPrice = float('inf')
        for p in prices:
            if p < minPrice: minPrice = p
            if p - minPrice > profit: profit = p - minPrice
        return profit