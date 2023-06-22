import bisect

n = int(input())
l1 = list(map(int, input().split()))
m = int(input())
l2 = list(map(int, input().split()))

l1.sort()

for val in l2:
    """
    left = 0
    right = len(l1) - 1
    ans = False
    while left <= right:
        mid = (left + right) // 2
        if l1[mid] == val:
            ans = True
            break
        elif l1[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    if ans:
        print("yes")
    else:
        print("no")
    """
    pos = bisect.bisect_left(l1, val)
    if pos < len(l1) and l1[pos] == val:
        print("yes")
    else:
        print("no")

