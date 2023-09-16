


def solution(m, n, board):
    def find_group():
        erased = 0
        board_cpy = [[col for col in row] for row in board]
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j] and board[i][j] == board[i+1][j+1]:
                    for k in range(2):
                        for l in range(2):
                            if board[i+k][j+l] != '.':
                                erased += 1
                            board_cpy[i+k][j+l] = '.'
        #board = board_cpy
        for i in range(m):
            for j in range(n):
                board[i][j] = board_cpy[i][j]
        return erased

    def move():
        for j in range(n):
            empty_row = -1
            for i in range(m-1, -1, -1):
                if board[i][j] == '.' and empty_row == -1:
                    empty_row = i
                elif board[i][j] != '.' and empty_row != -1:
                    board[empty_row][j] = board[i][j]
                    board[i][j] = '.'
                    empty_row += 1

    answer = 0
    while True:
        ret = find_group()
        if ret == 0:
            break
        answer += ret
    return answer


board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
ret = solution(4, 5, board)
print(ret)