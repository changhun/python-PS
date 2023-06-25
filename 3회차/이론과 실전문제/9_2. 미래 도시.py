import heapq
import collections

# 다익스트라까지 필요 없이 그냥 BFS 로 풀린다. 두 가지 다 해보기.

""" sol1: dijkstra """
"""
INF = int(1e9)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
# 거리가 다 1 이므로 edge 를 tuple 로 표현하지 않아도 된다.
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

X, K = map(int, input().split())

distance = [INF] * (N + 1)

def dijkstra(start):
    pq = []
    distance[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        here_dist, here = heapq.heappop(pq)

        # dijkstra 처음 작성하면 항상 이 조건때문에 한번은 fail 하는 듯
        #if distance[here] <= here_dist:
        if distance[here] < here_dist:
            continue

        for there in graph[here]:
            there_dist = here_dist + 1
            if distance[there] <= there_dist:
                continue
            distance[there] = there_dist
            heapq.heappush(pq, (there_dist, there))


dijkstra(K)
ans = distance[1] + distance[X]
if ans >= INF:
    print(-1)
else:
    print(ans)
"""

""" sol2: BFS """
"""
INF = int(1e9)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
# 거리가 다 1 이므로 edge 를 tuple 로 표현하지 않아도 된다.
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

X, K = map(int, input().split())

distance = [INF] * (N + 1)

def bfs(start):
    q = collections.deque()
    distance[start] = 0
    q.append(start)

    while q:
        here = q.popleft()

        for there in graph[here]:
            if distance[there] != INF:
                continue
            distance[there] = distance[here] + 1
            q.append(there)


bfs(K)
ans = distance[1] + distance[X]
if ans >= INF:
    print(-1)
else:
    print(ans)
"""


""" sol3: Floyd """
INF = int(1e9)

N, M = map(int, input().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]
# 거리가 다 1 이므로 edge 를 tuple 로 표현하지 않아도 된다.
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, N+1):
    graph[i][i] = 0

X, K = map(int, input().split())

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

ans = graph[1][K] + graph[K][X]
if ans >= INF:
    print(-1)
else:
    print(ans)