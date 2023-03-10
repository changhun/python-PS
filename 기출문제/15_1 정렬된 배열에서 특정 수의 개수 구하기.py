# x 이상의 값을 가지는 가장 작은 인덱스
def lower_bound(nums, x):
    s = 0
    e = len(nums) - 1
    ans = -1

    while s <= e:
        m = (s + e)//2
        if nums[m] >= x:
            ans = m
            e = m - 1
        else:
            s = m + 1

    return ans


# x 초과의 값을 가지는 가장 작은 인덱스
def upper_bound(nums, x):
    s = 0
    e = len(nums) - 1
    ans = -1

    while s <= e:
        m = (s + e)//2
        if nums[m] > x:
            ans = m
            e = m - 1
        else:
            s = m + 1

    return ans


N, x = map(int, input().split())
nums = list(map(int, input().split()))

low = lower_bound(nums, x)
up = upper_bound(nums, x)
if low == -1:
    print(-1)
else:
    if up == -1:
        up = len(nums)
    print(up - low)


# Input
#7 4
#1 1 2 2 2 2 3

#7 2
#1 1 2 2 2 2 3
