from collections import deque
import heapq

INF = int(1e9)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def dijkstra(sy, sx):
    heap = []
    heapq.heappush(heap, (graph[sy][sx], sy, sx))
    distance[sy][sx] = graph[sy][sx]

    while heap:
        dist, y, x = heapq.heappop(heap)
        if y == n-1 and x == n-1:
            return dist
        if distance[y][x] < dist:
            continue

        for di in range(4):
            ny = y + dy[di]
            nx = x + dx[di]
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if distance[ny][nx] <= dist + graph[ny][nx]:
                continue
            distance[ny][nx] = dist + graph[ny][nx]
            heapq.heappush(heap, (distance[ny][nx], ny, nx))


tc = int(input())
for _ in range(tc):
    n = int(input())
    distance = [[INF] * (n+1) for _ in range(n+1)]
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    ret = dijkstra(0, 0)
    print(ret)
