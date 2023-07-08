n, m = map(int ,input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))


def dfs(board, sy, sx, remain):
    if remain == 0:
        bfs(board)
        return