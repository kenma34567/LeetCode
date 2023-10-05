class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buyPrice = prices[0]

        maxProfit = 0

        for i in range(1, len(prices)):
            sellPrice = prices[i]
            if sellPrice < buyPrice:
                buyPrice = sellPrice
                continue

            maxProfit = max(maxProfit, sellPrice - buyPrice)

        return maxProfit
