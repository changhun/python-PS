from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

N, K = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

S, Y, X = map(int, input().split())

distance = [[INF]*N for _ in range(N)]
virus_list = []
for i in range(N):
    for j in range(N):
        if board[i][j] > 0:
            virus_list.append([board[i][j], i, j])
            distance[i][j] = 0

"""
virus_list.sort()
q = deque(virus_list)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
while q:
    virus_num, y, x = q.popleft()
    if distance[y][x] == S:
        break

    for di in range(4):
        ny = y + dy[di]
        nx = x + dx[di]
        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            continue
        if distance[ny][nx] != INF:
            continue
        board[ny][nx] = virus_num
        distance[ny][nx] = distance[y][x] + 1
        q.append([virus_num, ny, nx])
"""
#"""
virus_list.sort()
virus_positions = []
for virus in virus_list:
    virus_positions.append((virus[1], virus[2]))
q = deque(virus_positions)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
while q:
    y, x = q.popleft()
    if distance[y][x] == S:
        break

    for di in range(4):
        ny = y + dy[di]
        nx = x + dx[di]
        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            continue
        if distance[ny][nx] != INF:
            continue
        board[ny][nx] = board[y][x]
        distance[ny][nx] = distance[y][x] + 1
        q.append([ny, nx])
#"""

print(board[Y-1][X-1])
