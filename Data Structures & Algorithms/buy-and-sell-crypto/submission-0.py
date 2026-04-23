class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0 
        maxProfit = 0 
        minPrice = prices[0]
        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)
        return maxProfit