class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        profit = 0
        minTrade = prices[0]
        
        for price in prices[1:]:
            if price < minTrade:
                minTrade = price
            elif profit < (price-minTrade):
                profit = price-minTrade
                
        return profit
                