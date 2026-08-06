class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_so_far = prices[0]
        max_profit_so_far = 0

        for price in prices:
            if price < min_price_so_far:
                min_price_so_far = price

            potential_profit = price - min_price_so_far

            if potential_profit > max_profit_so_far:
                max_profit_so_far = potential_profit

        return max_profit_so_far

            



