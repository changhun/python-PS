import collections
INF = int(1e9)
n, m, k, x = map(int, input().split())
graph = collections.defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

ans = 0
dist = [INF]*(n+1)
dist[x] = 0
q = collections.deque()
q.append(x)
while q:
    here = q.popleft()
    if dist[here] > k:
        break
    if dist[here] == k:
        ans += 1

    for there in graph[here]:
        if dist[there] == INF:
            dist[there] = dist[here] + 1
            q.append(there)

if ans == 0:
    print(-1)
else:
    print(ans)