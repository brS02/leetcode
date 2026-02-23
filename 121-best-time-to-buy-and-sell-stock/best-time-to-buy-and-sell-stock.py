class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minp = prices[0]
        result = 0

        for price in prices:
            if minp > price:
                minp = price

            result = max(result, price - minp)

        return result