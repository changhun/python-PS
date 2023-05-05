MAX_N = 30

class Solution:
    def fib(self, n: int) -> int:
        memo = [-1] * (MAX_N + 2)
        memo[0] = 0
        memo[1] = 1
        for i in range(2, n+1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]