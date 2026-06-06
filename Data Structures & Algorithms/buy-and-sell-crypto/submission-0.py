class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        final_profit = 0
        profit = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):

                if prices[i] < prices[j]:
                    profit = prices[j] - prices[i]

                    if profit > final_profit:
                        final_profit = profit

        return final_profit

