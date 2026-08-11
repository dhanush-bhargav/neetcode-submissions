class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for t in range(1,len(prices)):
            if prices[t-1]<prices[t]:
                profit += prices[t] - prices[t-1]
        return profit
        
