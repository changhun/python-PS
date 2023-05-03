from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        has_stock = False
        profit = 0

        for i in range(len(prices) -1):
            if has_stock and prices[i] > prices[i + 1]:
                profit += prices[i]
                has_stock = False
            elif not has_stock and prices[i] < prices[i + 1]:
                profit -= prices[i]
                has_stock = True
        if has_stock:
            profit += prices[-1]

        return profit