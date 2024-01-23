n = int(input())
fear = list(map(int, input().split()))

fear.sort()
ans = 0
s = 0
for e in range(n):
    if e - s + 1 >= fear[e]:
        ans += 1
        s = e + 1

print(ans)