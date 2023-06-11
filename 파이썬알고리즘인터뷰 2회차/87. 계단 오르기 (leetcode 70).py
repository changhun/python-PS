MAX_STEPS = 45

class Solution:
    dp = [-1] * (MAX_STEPS + 1)
    def climbStairs(self, n: int) -> int:
        if 0 <= n <= 1:
            return 1

        if self.dp[n] != -1:
            return self.dp[n]

        self.dp[n] = self.climbStairs(n-2) + self.climbStairs(n-1)
        return self.dp[n]
