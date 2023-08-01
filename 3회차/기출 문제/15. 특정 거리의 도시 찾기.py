import collections
import sys

input = sys.stdin.readline


n, m, k, x = map(int, input().split())
adj = collections.defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)

dist = [-1] * (n+2)
q = collections.deque()
q.append(x)
dist[x] = 0
while q:
    here = q.popleft()
    for there in adj[here]:
        if dist[there] == -1:
            dist[there] = dist[here] + 1
            q.append(there)

ans = [i for i, val in enumerate(dist) if val == k]

if not ans:
    print(-1)
else:
    for city in ans:
        print(city)