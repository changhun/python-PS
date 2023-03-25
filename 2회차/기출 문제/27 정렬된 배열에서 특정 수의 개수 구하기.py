def lower_bound(nums, x):
    n = len(nums)
    ans = n
    s, e = 0, n-1

    while s <= e:
        m = (s+e)//2
        if nums[m] >= x:
            ans = m
            e = m - 1
        else:
            s = m + 1

    return ans


def upper_bound(nums, x):
    n = len(nums)
    ans = n
    s, e = 0, n - 1

    while s <= e:
        m = (s + e) // 2
        if nums[m] > x:
            ans = m
            e = m - 1
        else:
            s = m + 1

    return ans


n, x = map(int, input().split())
nums = list(map(int, input().split()))

lower = lower_bound(nums, x)
upper = upper_bound(nums, x)
ans = upper - lower
if ans > 0:
    print(ans)
else:
    print(-1)