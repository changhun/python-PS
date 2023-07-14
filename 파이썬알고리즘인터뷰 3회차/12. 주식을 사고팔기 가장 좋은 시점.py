INF = int(1e9)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        ans = 0
        min_val = INF
        max_val = -INF
        for price in prices:
            if price > max_val:
                max_val = price
            if price < min_val:
                min_val = price
                max_val = price
            ans = max(ans, max_val - min_val)
        return ans


prices = [7, 1, 5, 3, 6, 4]
prices = [7,6,4,3,1]
ans = Solution().maxProfit(prices)
print(ans)