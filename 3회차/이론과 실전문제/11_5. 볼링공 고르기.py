import collections

n, m = map(int, input().split())
sizes = list(map(int, input().split()))

counts = collections.Counter(sizes)
print(counts.values())
counts = list(counts.values())
p_sum = counts[:]
for i in range(len(p_sum) - 2, -1, -1):
    p_sum[i] += p_sum[i + 1]

ans = 0
for i in range(len(p_sum) - 1):
    ans += counts[i] * p_sum[i+1]
print(ans)