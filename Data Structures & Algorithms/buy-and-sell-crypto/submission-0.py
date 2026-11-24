class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfit = float('-inf')
        for p in prices:
            if p < minPrice: minPrice = p
            if p - minPrice > maxProfit: maxProfit = p - minPrice
        return maxProfit