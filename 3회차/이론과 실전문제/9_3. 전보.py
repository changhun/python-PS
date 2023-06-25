import heapq

INF = int(1e9)
N, M, START = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))

dists = [INF] * (N + 1)
dists[START] = 0
pq = []
heapq.heappush(pq, (0, START))

while pq:
    dist_here, here = heapq.heappop(pq)
    if dists[here] < dist_here:
        continue

    for there, edge_cost in adj[here]:
        dist_there = dist_here + edge_cost
        if dists[there] <= dist_there:
            continue
        dists[there] = dist_there
        heapq.heappush(pq, (dist_there, there))

    cities = [dist for dist in dists if dist != INF and dist != 0]
print(len(cities), max(cities))
