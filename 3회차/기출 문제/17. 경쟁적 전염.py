import collections
n, k = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().aplit())))

row, col = map(int, input.split())

virus = []
for i, row in enumerate(board):
    for j, num in enumerate(row):
        virus.append((num, i, j))

virus.sort()
q = collections.deque(virus)
print(q)

