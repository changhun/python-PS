n, m = map(int, input().split())
board_str = []
for _ in range(n):
    board_str.append(input())

board = []
for i, s in enumerate(board_str):
    board.append([])
    for char in s:
        board[i].append(int(char))
for low in board:
    print(low)


# Input
# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111
#
# 4 5
# 00110
# 00011
# 11111
# 00000