from collections import deque

EMPTY = 0
N, K = map(int, input().split())
#board = [[] for _ in range(N)]
board = []
distance = [[0]*N for _ in range(N)]
virus_list = []


for i in range(N):
    board.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if board[i][j] > 0:
            virus_list.append((i, j))

#print(virus_list)
virus_list.sort(key=lambda x: board[x[0]][x[1]])
#print(virus_list)

S, ROW, COL = map(int, input().split())
ROW -= 1
COL -= 1

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def virus_simulation():
    q = deque(virus_list)

    while q:
        y, x = q.popleft()
        if distance[y][x] >= S:
            break

        for di in range(4):
            ny = y + dy[di]
            nx = x + dx[di]
            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] == EMPTY:
                distance[ny][nx] = distance[y][x] + 1
                board[ny][nx] = board[y][x]
                q.append((ny, nx))
    print(board[ROW][COL])

virus_simulation()

