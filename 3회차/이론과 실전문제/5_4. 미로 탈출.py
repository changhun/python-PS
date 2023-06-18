import collections
N, M = map(int, input().split())

"""
board_str = []
for _ in range(N):
    board_str.append(input())

board = []
for i, low in enumerate(board_str):
    board.append([])
    for char in low:
        board[i].append(int(char))
"""
board = []
for i in range(N):
    board.append(list(map(int, input())))

move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def bfs(graph, y, x):
    q = collections.deque()
    q.append((y, x, 1))
    board[y][x] = 0
    while q:
        y, x, dist = q.popleft()
        if y == N - 1 and x == M - 1:
            return dist

        for m in move:
            ny = y + m[0]
            nx = x + m[1]
            if 0 <= ny <= N - 1 and 0 <= nx <= M - 1 and board[ny][nx] == 1:
                board[ny][nx] = 0
                q.append((ny, nx, dist + 1))

    return -1

ans = bfs(board, 0, 0)
print(ans)
