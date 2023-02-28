from collections import deque
from itertools import combinations

N, M = map(int, input().split())

board = [[] for _ in range(N)]
for i in range(N):
    board[i] = list(map(int, input().split()))
    # board[i] = [list(]map(int, input().split())] 이렇게 하면 안 됨. 왜 안 되지?



EMPTY = 0
WALL = 1
VIRUS = 2

empty_list = []
virus_list = []

ans = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == EMPTY:
            empty_list.append((i, j))
        elif board[i][j] == VIRUS:
            virus_list.append((i, j))


def count_empty_space(board):
    ret = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == EMPTY:
                ret += 1
    return ret


def set_wall(board, wall_list):
    for i, j in wall_list:
        board[i][j] = WALL
    #print(board)


def is_valid(low, col):
    if 0 <= low < N and 0 <= col < M:
        return True
    return False


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def calc_safe_space(board):
    q = deque(virus_list)
    while q:
        y, x = q.popleft()

        for di in range(4):
            ny = y + dy[di]
            nx = x + dx[di]
            if is_valid(ny, nx) and board[ny][nx] == EMPTY:
                board[ny][nx] = VIRUS
                q.append((ny, nx))

    ret = count_empty_space(board)
    return ret


board_copy = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        board_copy[i][j] = board[i][j]
# for Unit Test
# wall_list = [(0, 0), (1, 1), (2, 2)]
# set_wall(board_copy, wall_list)

ans = 0
for wall_list in combinations(empty_list, 3):
    board_copy = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            board_copy[i][j] = board[i][j]

    set_wall(board_copy, wall_list)

    ans = max(ans, calc_safe_space(board_copy))


print(ans)