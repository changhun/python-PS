N = int(input())
board = []
for i in range(N):
    board.append(list(input().split()))

#print(type(board[0][0]))

def is_ok(board, y, x):
    # 위로
    for ny in range(y-1, -1, -1):
        if board[ny][x] == 'S':
            return False
        if board[ny][x] == 'O' or board[ny][x] == 'T':
            break

    for ny in range(y+1, N):
        if board[ny][x] == 'S':
            return False
        if board[ny][x] == 'O' or board[ny][x] == 'T':
            break

    for nx in range(x-1, -1, -1):
        if board[y][nx] == 'S':
            return False
        if board[y][nx] == 'O' or board[y][nx] == 'T':
            break;

    for nx in range(x+1, N):
        if board[y][nx] == 'S':
            return False
        if board[y][nx] == 'O' or board[y][nx] == 'T':
            break;

    return True


def dfs(board, cnt):
    if cnt == 3:
        for i in range(N):
            for j in range(N):
                if board[i][j] == 'T':
                    ret = is_ok(board, i, j)
                    # 모든 선생님의 위치에서 학생이 안보여야 해결된거다.
                    if ret is False:
                        return False
        return True

    for i in range(N):
        for j in range(N):
            if board[i][j] == 'X':
                board[i][j] = 'O'
                ret = dfs(board, cnt+1)
                if ret is True:
                    return True
                board[i][j] = 'X'

    return False


ret = dfs(board, 0)
if ret is True:
    print("YES")
else:
    print("NO")