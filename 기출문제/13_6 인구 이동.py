# 백준 사이트의 경우 recursive 깊이 제한이 있어서 관련 설정을 해줘야 한다.
N, L, R = map(int, input().split())

board = []
for i in range(N):
    board.append(list(map(int, input().split())))


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def dfs(board, i, j, align_seq, seq):
    align_seq[i][j] = seq
    for di in range(4):
        ny = i + dy[di]
        nx = j + dx[di]
        if ny < 0 or ny >= N: continue
        if nx < 0 or nx >= N: continue
        if align_seq[ny][nx] != -1: continue
        if L <= abs(board[i][j] - board[ny][nx]) <= R:
            dfs(board, ny, nx, align_seq, seq)

# return if moving occurs
def move(board):
    seq = 0
    align_seq = [[-1] * N for _ in range(N)]
    align_sum = [0] * (N*N)
    align_size = [0] * (N*N)
    align_avg = [0] * (N*N)

    for i in range(N):
        for j in range(N):
            if align_seq[i][j] == -1:
                dfs(board, i, j, align_seq, seq)
                seq += 1

    if seq == N * N:
        return False

    for i in range(N):
        for j in range(N):
            align_sum[align_seq[i][j]] += board[i][j]
            align_size[align_seq[i][j]] += 1

    for i in range(seq):
        align_avg[i] = align_sum[i] // align_size[i]

    for i in range(N):
        for j in range(N):
            board[i][j] = align_avg[align_seq[i][j]]

    return True


day = 0
while move(board):
    day += 1

print(day)