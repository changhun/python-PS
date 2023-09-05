MAX_STEPS = 45

class Solution:
    dp = [-1] * (MAX_STEPS + 1)
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if self.dp[n] != -1:
            return self.dp[n]
        self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dp[n]
