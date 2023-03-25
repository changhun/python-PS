"""ver1
n = int(input())
times = [0]*n
prices = [0]*n

for i in range(n):
    times[i], prices[i] = map(int, input().split())

for i in range(n-1, -1, -1):
    max_val = 0
    val1 = val2 = 0
    if i+1 < n:
        val1 = prices[i+1]

    if i + times[i] <= n: # 현재 날짜 + 걸리는 날짜 < 퇴사날 이어야 해당 일을 할 수 있다. (index 의 경우 <= 퇴사날)
        val2 = prices[i]

    if i + times[i] < n:
        val2 += prices[i+times[i]]
    prices[i] = max(max_val, val1, val2)

print(prices[0])
"""

""" ver2 """
n = int(input())
times = [0]*n
prices = [0]*n
memo = [-1] * (n+1)

for i in range(n):
    times[i], prices[i] = map(int, input().split())


def dp(start):
    if start >= n:
        return 0
    if memo[start] != -1:
        return memo[start]

    max_val = dp(start+1)
    if start + times[start] <= n:
        max_val = max(max_val, prices[start] + dp(start + times[start]))
    memo[start] = max_val
    return memo[start]

ans = dp(0)
print(ans)
