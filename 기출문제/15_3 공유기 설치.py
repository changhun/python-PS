def is_ok(homes, min_len, remain):
    # remain 변수는 인자로 받아서 copy 해야됨? reference type 임?
    next_pos = homes[0] + min_len
    cur = 1
    remain -= 1

    i = 1
    while i < len(homes) and remain:
        if homes[i] >= next_pos:
            next_pos = homes[i] + min_len
            remain -= 1

        i += 1

    return remain == 0


def binary_search(nums, remains):
    s = 1
    e = nums[len(nums) - 1] - nums[0]
    ans = -1

    while s <= e:
        m = (s + e) // 2
        if is_ok(nums, m, remains):
            ans = m
            s = m + 1
        else:
            e = m - 1

    return ans


N, C = map(int, input().split())
homes = list(map(int, input().split()))
homes.sort()
ret = binary_search(homes, C)
print(ret)

