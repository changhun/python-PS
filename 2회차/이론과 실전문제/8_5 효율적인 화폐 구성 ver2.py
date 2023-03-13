import sys
input = sys.stdin.readline


INF = int(1e9)
N, M = map(int, input().split())
memo = [INF] * (M+1)

coins = []
for i in range(N):
    coins.append(int(input()))

memo[0] = 0
for i in range(M+1):
    if memo[i] != INF:
        for coin in coins:
            if i + coin > M:
                continue
            memo[i+coin] = min(memo[i] + 1, memo[i+coin])

if memo[M] == INF:
    print(-1)
else:
    print(memo[M])
