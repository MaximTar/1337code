from typing import List


class Solution:
    # first try (bad try)
    def maxProfit(self, prices: List[int]) -> int:
        len_prices = len(prices)
        max_profit = 0
        for i in range(len_prices - 1):
            price_i = prices[i]
            for j in range(i + 1, len_prices):
                price_j = prices[j]
                if price_j > price_i:
                    profit = price_j - price_i
                    if profit > max_profit:
                        max_profit = profit
        return max_profit

    # two pointers
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, buy_pointer_idx, sell_pointer_idx = 0, 0, 1
        while sell_pointer_idx < len(prices):
            profit = prices[sell_pointer_idx] - prices[buy_pointer_idx]
            if profit < 0:
                buy_pointer_idx = sell_pointer_idx
            elif profit > max_profit:
                max_profit = profit
            sell_pointer_idx += 1
        return max_profit

    # from discussions
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            min_price = min(price, min_price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
