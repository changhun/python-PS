import collections


n, m, k, x = map(int, input().split())
adj = collections.defaultdict(list)
for _ in range(m):
    u, v = map(int, input())
    adj[u].append(v)

dist = [-1] * (n+2)
q = collections.deque()
q.append(x)
dist[x] = 0
while q:
    here = q.popleft()
    for there in adj[here]:
        if dist[there] != -1:
            dist[there] = dist[here] + 1
            q.append(there)
ans = dist.count(k)
if ans == 0:
    ans = -1
print(ans)