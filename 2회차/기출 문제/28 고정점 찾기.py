

def binary_search(nums):
    ans = -1
    s, e = 0, len(nums) - 1

    while s <= e:
        m = (s+e)//2
        if nums[m] == m:
            return m
        elif nums[m] < m:
            s = m + 1
        elif nums[m] > m:
            e = m - 1
    return ans

n = int(input())
nums = list(map(int, input().split()))
ret = binary_search(nums)
print(ret)
