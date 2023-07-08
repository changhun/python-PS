import collections
EMPTY = 0
WALL = 1
VIRUS = 2

n, m = map(int ,input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))


ans = 0

def dfs(board, sy, sx, remain):
    if remain == 0:
        bfs(board)
        return

    if sy < 0 or sy >= n or sx < 0 or sx >= m:
        return

    for x in range(sx, m):
        if board[sy][x] == EMPTY:
            board[sy][x] = WALL
            ny, nx = sy, x + 1
            if nx >= m:
                ny += 1
                nx = 0
            dfs(board, ny, nx, remain - 1)
            board[sy][x] = EMPTY

    for y in range(sy + 1, n):
        for x in range(m):
            if board[y][x] == EMPTY:
                board[y][x] = WALL
                ny, nx = y, x + 1
                if nx >= m:
                    ny += 1
                    nx = 0
                dfs(board, ny, nx, remain - 1)
                board[y][x] = EMPTY

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
def bfs(board):
    board_cpy = [row[:] for row in board]
    q = collections.deque()
    for i in range(n):
        for j in range(m):
            if board_cpy[i][j] == VIRUS:
                q.append((i, j))
    while q:
        y, x = q.popleft()
        for di in range(4):
            ny = y + dy[di]
            nx = x + dx[di]
            if ny < 0 or ny >= n:
                continue
            if nx < 0 or nx >= m:
                continue
            if board_cpy[ny][nx] == EMPTY:
                q.append((ny, nx))
                board_cpy[ny][nx] = VIRUS

    safe_count = 0
    for row in board_cpy:
        safe_count += row.count(EMPTY)
    global ans
    ans = max(ans, safe_count)


dfs(board, 0, 0, 3)
print(ans)
