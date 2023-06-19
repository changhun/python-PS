n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
#b.sort(key=reversed)
b.sort(reverse=True)
#b = list(reversed(b))

for i in range(k):
    a[i], b[i] = b[i], a[i]

print(sum(a))