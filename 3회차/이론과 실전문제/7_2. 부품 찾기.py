import bisect

n = int(input())
l1 = list(map(int, input().split()))
m = int(input())
l2 = list(map(int, input().split()))

l1.sort()

for val in l2:
    left = 0
    right = len(l1) - 1
    while left < right:
        mid = (left + right) // 2
        if l1[mid] == val:
            break
        elif l1[mid] < val:
            left = mid
        else:
            right = mid
    if l1[mid] == val:
        print("yes")
    else:
        print("no")

    #pos = bisect.bisect_left()
