import collections
import sys
input = sys.stdin.readline

INF = int(1e9)
n, m, k, x = map(int, input().split())

#graph = collections.defaultdict(list)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

ans = []
dist = [INF]*(n+1)
dist[x] = 0
q = collections.deque()
q.append(x)
while q:
    here = q.popleft()
    """
    if dist[here] > k:
        break
    if dist[here] == k:
        ans.append(here)
    """

    for there in graph[here]:
        if dist[there] == INF:
            dist[there] = dist[here] + 1
            q.append(there)

for i, val in enumerate(dist):
    if val == k:
        ans.append(i)

#if not ans:
if len(ans) == 0:
    print(-1)
else:
    for val in ans:
        print(val)