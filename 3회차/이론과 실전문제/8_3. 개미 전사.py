""" sol1: bottom up"""
"""
n = int(input())
nums = list(map(int, input().split()))
ans = [0] * n
ans[n-1] = nums[n-1]
ans[n-2] = max(nums[n-2], nums[n-1])
for i in range(n-3, -1, -1):
    ans[i] = max(ans[i+1], nums[i] + ans[i+2])

print(ans[0])
"""

""" sol2: top down (memoization) """
n = int(input())
nums = list(map(int, input().split()))
dp = [-1] * n

def memoization(start):
    if start >= n:
        return 0

    if dp[start] != -1:
        return dp[start]

    ret = nums[start] + memoization(start + 2)
    ret = max(ret, memoization(start + 1))
    dp[start] = ret
    return dp[start]


ret = memoization(0)
print(ret)
