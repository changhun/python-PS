INF = int(1e9)
MAX_TOTAL = int(1e5) + 2

n, total = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [INF] * MAX_TOTAL
dp[0] = 0
for i in range(1, total + 1):
    for coin in coins:
        if i - coin >= 0:
            dp[i] = min(dp[i], dp[i-coin] + 1)

if dp[total] < INF:
    print(dp[total])
else:
    print(-1)