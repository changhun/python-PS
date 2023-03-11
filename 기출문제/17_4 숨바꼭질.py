from collections import deque
INF = int(1e9)
N, M = map(int, input().split())

adj = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)


dist = [INF]*(N+1)
dist[1] = 0
q = deque()
q.append(1)


while q:
    here = q.popleft()

    for there in adj[here]:
        if dist[there] != INF:
            continue

        dist[there] = dist[here] + 1
        q.append(there)

max_val = max(dist[1:])
max_list = []
for i in range(1, N+1):
    if dist[i] == max_val:
        max_list.append(i)

min_room = min(max_list)
print(f"{min_room} {max_val} {len(max_list)}")