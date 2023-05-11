class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_val = prices[0]
        ans = 0
        for price in prices[1:]:
            ans = max(ans, price - min_val)
            min_val = min(min_val, price)
        return ans