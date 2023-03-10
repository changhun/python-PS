def binary_search(nums):
    s = 0
    e = len(nums) - 1
    ans = -1
    while s <= e:
        m = (s + e) // 2
        if nums[m] == m:
            return m
        elif nums[m] < m:
            s = m + 1
        else:
            e = m - 1

    return ans


N = int(input())
nums = list(map(int, input().split()))

ret = binary_search(nums)
print(ret)


# Input
# 7
# -15 -4 3 8 9 13 15
#
# 7
# -15 -4 2 8 9 13 15
#
# 5
# -15 -6 -1 3 7