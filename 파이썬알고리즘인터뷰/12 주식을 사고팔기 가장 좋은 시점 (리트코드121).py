class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        max_val = [0] * n
        max_val[-1] = prices[-1]
        ans = 0
        for i in range(n-2, -1, -1):
            max_val[i] = max(prices[i], max_val[i+1])

        for i in range(n-1):
            ans = max(ans, max_val[i+1] - prices[i])

        return ans


prices = [7,6,4,3,1]
sol = Solution()
ret = sol.maxProfit(prices)
print(ret)