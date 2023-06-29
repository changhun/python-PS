n = int(input())
fears = list(map(int, input().split()))

fears.sort()

s = 0
ans = 0
for i, fear in enumerate(fears):
    if i - s + 1 >= fear:
        ans += 1
        s = i + 1

print(ans)
