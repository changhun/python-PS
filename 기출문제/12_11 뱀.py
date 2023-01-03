# 클래스로도 작성해보기!!!

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
# DIR = ['N', 'E', 'S', 'W']
# enum, const 어떻게 하지?
N = 0
E = 1
S = 2
W = 3

EMPTY = 0
APPLE = 1

N = int(input())
board = [[0] * N for _ in range(N)]

K = int(input())
# apples = []
for i in range(K):
    # apples.append(tuple(map(int, input().split())))
    y, x = map(int, input().split())
    board[y][x] = APPLE

L = int(input())
move_info_time = []
move_info_dir = []
for i in range(L):
    time, dir = input().split()
    move_info_time.append(int(time))
    move_info_dir.append(dir)


def move_left(direction) -> int:
    direction = (direction + 4 - 1) % 4
    return direction


def move_right(direction) -> int:
    direction = (direction + 1) % 4
    return direction