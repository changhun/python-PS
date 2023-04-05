
"""
def getMaxGroup(nums):
    nums.sort()

    ans = 0
    s = 0

    while s < len(nums):
        cnt = 1
        i = 0
        while s + i < len(nums):
            if cnt >= nums[s + i]:
                ans += 1
                break
            cnt += 1
            i += 1
        s += i + 1

    return ans
"""

def getMaxGroup(nums):
    nums.sort()
    ans = 0
    s, i, cnt = 0, 0, 1
    while s+i < n:
        if cnt >= nums[s+i]:
            ans += 1
            s += i + 1
            i, cnt = 0, 1
        else:
            i += 1
            cnt += 1
    return ans


n = int(input())
nums = list(map(int, input().split()))
ret = getMaxGroup(nums)
print(ret)