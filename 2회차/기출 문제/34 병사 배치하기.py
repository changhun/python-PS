# dp(start) 함수는 start 포함 해야한다.
# 포함 할수도 있고 안 할수도 있는 함수로 정의하면 앞에서 선택된 최저값에 따라 start를 포함 못 할 수도 있다.

"""ver1
import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))

dp = [0]*(n+1)
dp[n-1] = 1
for i in range(n-2, -1, -1):
    max_val = 0
    for j in range(i+1, n):
        if nums[i] > nums[j]:
            max_val = max(max_val, dp[j])

    max_val += 1 # i번 병사 포함
    dp[i] = max_val

print(n - max(dp))
"""

"""ver2"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
nums = list(map(int, input().split()))
memo = [-1] * (n+1)


def dp(start):
    if start >= n:
        return 0
    if memo[start] != -1:
        return memo[start]

    next_lds = 0
    for next_start in range(start+1, n):
        if nums[next_start] < nums[start]:
            next_lds = max(next_lds, dp(next_start))
    memo[start] = next_lds + 1
    return memo[start]


max_val = 0
for i in range(n):
    max_val = max(max_val, dp(i))
print(n - max_val)