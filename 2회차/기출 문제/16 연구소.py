from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1

      ]
def bfs(board):
    n = len(board)
    m = len(board[0])
    q = deque()
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                q.append((i, j))
    while q:
        y, x = q.popleft()
        for di in range(4):
            ny = y + dy[di]
            nx = x + dx[di]
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            if board[ny][nx] == 0:
                board[ny][nx] = 2
                q.append((ny, nx))

    safe_cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                safe_cnt += 1
    return safe_cnt


N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

positions = [(i, j) for i in range(N) for j in range(M)]
#print(positions)
ans = 0
for comb in combinations(positions, 3):
    #print(comb)
    #copied = [board[i][j] for i in range(N) for j in range(M)]
    copied = [[board[i][j] for j in range(M)] for i in range(N)]
    #print(copied)
    cont = False
    for i, j in comb:
        if board[i][j] != 0:
            cont = True
            break
        copied[i][j] = 1
    if cont:
        continue

    ret = bfs(copied)
    ans = max(ans, ret)
print(ans)
