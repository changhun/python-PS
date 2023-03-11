import heapq
INF = int(1e9)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def dijkstra(board):
    board_size = len(board)
    distance = [[INF]*(board_size) for _ in range(board_size)]
    heap = [(board[0][0], 0, 0)]
    #heapq.heapify(heap)

    # empty 조건문 어떻게 해?
    #while len(heap):
    while heap:
        dist, y, x = heapq.heappop(heap)

        distance[y][x] = min(distance[y][x], dist)
        for di in range(4):
            ny = y + dy[di]
            nx = x + dx[di]
            if ny < 0 or ny >= board_size:
                continue
            if nx < 0 or nx >= board_size:
                continue
            if distance[ny][nx] != INF:
                continue
            heapq.heappush(heap, (dist + board[ny][nx], ny, nx))

    return distance[board_size-1][board_size-1]


T = int(input())

for _ in range(T):
    N = int(input())

    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    ret = dijkstra(graph)
    print(ret)

