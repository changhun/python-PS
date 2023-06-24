MAX_N = int(3e4) + 2
INF = int(2e9)
# import sys
# INF = sys.maxsize
n = int(input())

""" sol1: memoization """
"""
dp = [-1] * MAX_N
def make1(cur_val):
    if cur_val == 1:
        return 0

    if cur_val <= 0:
        return INF

    if dp[cur_val] != -1:
        return dp[cur_val]

    ret = make1(cur_val - 1) + 1
    if cur_val % 5 == 0:
        ret = min(ret, make1(cur_val//5) + 1)
    if cur_val % 3 == 0:
        ret = min(ret, make1(cur_val//3) + 1)
    if cur_val % 2 == 0:
        ret = min(ret, make1(cur_val//2) + 1)

    dp[cur_val] = ret
    return dp[cur_val]

ret = make1(n)
print(ret)
"""
""" sol2: bottom up """

dp = [INF] * (n + 2)
# n - 1 까지만 loop 돌면 된다.
dp[1] = 0
for i in range(1, n):
    if i * 5 <= n:
        dp[i * 5] = min(dp[i * 5], dp[i] + 1)
    if i * 3 <= n:
        dp[i * 3] = min(dp[i * 3], dp[i] + 1)
    if i * 2 <= n:
        dp[i * 2] = min(dp[i * 2], dp[i] + 1)
    if i + 1 <= n:
        dp[i + 1] = min(dp[i + 1], dp[i] + 1)

print(dp[n])

