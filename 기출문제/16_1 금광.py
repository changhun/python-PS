
def get_max_gold(row, col, board, memo):
    if col >= len(board[0]) or row < 0 or row >= len(board):
        return 0

    if memo[row][col] != -1:
        return memo[row][col]

    ret = board[row][col] + get_max_gold(row - 1, col + 1, board, memo)
    for next_row in range(row, row + 2):
        ret = max(ret, board[row][col] + get_max_gold(next_row, col + 1, board, memo))

    memo[row][col] = ret

    return ret

T = int(input())
for i in range(T):
    n, m = map(int, input().split())
    golds = list(map(int, input().split()))
    board = []
    memo = [[-1]*m for _ in range(n)]
    for i in range(n):
        board.append(golds[i*m:(i+1)*m])

    ans = 0
    for row in range(0, n):
        ans = max(ans, get_max_gold(row, 0, board, memo))
    print(ans)