
# Let's change 2D list type board in Snake to dictionary

EMPTY = 0
APPLE = 1

NORTH = 0
RIGHT = 1
DOWN = 2
LEFT = 3

DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class Snake:
    body = [(0, 0)]
    cur_dir = RIGHT
    cur_time = 0
    # board = []
    def __init__(self, _board):
        self.y = self.x = 0
        self.cur_dir = RIGHT
        self.board = _board
        self.N = len(self.board)
        self.M = len(self.board[0])

    def move(self):
        self.cur_time += 1

        ny = self.body[-1][0] + DIR[self.cur_dir][0]
        nx = self.body[-1][1] + DIR[self.cur_dir][1]

        if ny < 0 or ny >= self.N or nx < 0 or nx >= self.M:
            return False

        for y, x in self.body:
            if ny == y and nx == x:
                return False

        if self.board[ny][nx] == APPLE:
            self.body.append((ny, nx))
            self.board[ny][nx] = EMPTY
        else:
            for i in range(len(self.body) - 1):
                self.body[i] = self.body[i+1]
            self.body[-1] = (ny, nx)
        return True

    def turn(self, turn_dir):
        if turn_dir == RIGHT:
            self.cur_dir = (self.cur_dir + 1) % 4
        elif turn_dir == LEFT:
            self.cur_dir = (self.cur_dir -1 + 4) % 4

    def get_time(self):
        return self.cur_time


board_size = int(input())
K = int(input())
board = [[0]*board_size for _ in range(board_size)]
for i in range(K):
    y, x = map(int, input().split())
    board[y-1][x-1] = APPLE

L = int(input())
insts = []
for _ in range(L):
    X, D = input().split()
    X = int(X)
    if D == 'D':
        D = RIGHT
    elif D == 'L':
        D = LEFT
    insts.append((X, D))


snake = Snake(board)

is_end = False
for X, D in insts:
    while snake.get_time() < X:
        ret = snake.move()
        if not ret:
            is_end = True
            break
    if is_end:
        break
    snake.turn(D)

while not is_end:
    ret = snake.move()
    if not ret:
        is_end = True

print(snake.cur_time)