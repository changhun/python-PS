import sys
input = sys.stdin.readline


def solution(num: int, coins, memo) -> int:
    if num == 0:
        return 0
    elif num < 0:
        return INF

    if memo[num] != INF:
        return memo[num]

    ret = INF
    for coin in coins:
        ret = min(ret, solution(num - coin, coins, memo))
    memo[num] = ret + 1
    return memo[num]


INF = int(1e9)
N, M = map(int, input().split())
memo = [INF] * (M+1)

coins = []
for i in range(N):
    coins.append(int(input()))

ret = solution(M, coins, memo)
if ret >= INF:
    print(-1)
else:
    print(ret)

