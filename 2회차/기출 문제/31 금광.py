# 동적프로그래밍은 두가지 방식이 있다. top down, bottom up 방식. top down 은 재귀사용.
"""ver1
def get_max_path(board, y, x, n, m, memo):
    if y < 0 or y >= n or x >= m:
        return 0

    if memo[y][x] != -1:
        return memo[y][x]

    max_val = 0
    for ny in range(y-1, y+2):
        max_val = max(max_val, get_max_path(board, ny, x+1, n, m, memo))
    memo[y][x] = board[y][x] + max_val
    return memo[y][x]


tc = int(input())
for _ in range(tc):
    n, m = map(int ,input().split())
    memo = [[-1] * m for _ in range(n)]
    nums = list(map(int, input().split()))
    board = [nums[i*m:(i+1)*m] for i in range(n)]
    #print(board)

    max_val = 0
    for i in range(n):
        max_val = max(max_val, get_max_path(board,i, 0, n, m, memo))
    print(max_val)
"""

""" ver2 """
tc = int(input())
for _ in range(tc):
    n, m = map(int ,input().split())
    nums = list(map(int, input().split()))
    board = [nums[i*m:(i+1)*m] for i in range(n)]

    for j in range(1, m):
        for i in range(n):
            max_val = board[i][j-1]
            if i-1 >= 0:
                max_val = max(max_val, board[i-1][j-1])
            if i+1 < n:
                max_val = max(max_val, board[i+1][j-1])
            board[i][j] += max_val

    max_val = 0
    for i in range(n):
        max_val = max(max_val, board[i][m-1])
    print(max_val)