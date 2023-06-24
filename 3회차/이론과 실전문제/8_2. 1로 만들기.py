MAX_N = int(3e4) + 2
INF = int(2e9)
#import sys
#INF = sys.maxsize
n = int(input())

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