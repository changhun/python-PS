N = int(input())
nums = list(map(int, input().split()))
dp = [0] * N

for i in range(N-1, -1, -1):
    next_lds = 0
    for j in range(i+1, N):
        if nums[i] > nums[j]:
            next_lds = max(next_lds, dp[j])
    dp[i] = next_lds + 1


print(N - max(dp))
