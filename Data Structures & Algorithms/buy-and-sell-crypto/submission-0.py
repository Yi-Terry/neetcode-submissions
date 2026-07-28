class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for current in range(len(prices)):
            for future in range(current, len(prices)):
                current_profit = prices[future] - prices[current]

                if current_profit > max_profit:
                    max_profit = current_profit
        return max_profit
