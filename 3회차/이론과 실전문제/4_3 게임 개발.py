WATER = 1
LAND = 0

n, m = map(int, input().split())
y, x, dir = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


game_over = False
turn_count = 0
visit_count = 0

while not game_over:
    if board[y][x] == LAND:
        visit_count += 1
        board[y][x] = WATER

    if turn_count == 4:
        ny, nx = y - dy[dir], x - dx[dir]
        if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == LAND:
            y = ny
            x = nx
            turn_count = 0
        else:
            game_over = True
            break

    dir = (dir + 1) % 4
    ny, nx = y - dy[dir], x - dx[dir]
    if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == LAND:
        y, x = ny, nx
        turn_count = 0
    else:
        turn_count += 1


print(visit_count)