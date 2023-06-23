n, m = map(int, input().split())
heights = list(map(int, input().split()))

def is_ok(heights, m, cut_line):
    total = 0
    for h in heights:
        total += max(0, h - cut_line)
    return total >= m

lo, hi = 0, max(heights)

ans = -1
while lo <= hi:
    mid = (lo + hi) // 2
    if is_ok(heights, m, mid):
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(ans)


