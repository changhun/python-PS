


def solution(key, lock):
    def rotate(board):
        n = len(board)
        rotated = [row[:] for row in board]
        for i in range(n):
            for j in range(n):
                rotated[j][n-i-1] = board[i][j]

        return rotated

    def check(key, lock):
        n = len(lock)
        m = len(key)
        for si in range(-m + 1, n):
            for sj in range(-m+1, n):
                lock_copied = [row[:] for row in lock]
                not_matched = False
                for ki in range(m):
                    if not_matched:
                        break
                    for kj in range(m):
                        li = si + ki
                        lj = sj + kj

                        if 0 <= li < n and 0 <= lj < n:
                            lock_copied[li][lj] += key[ki][kj]
                            if lock_copied[li][lj] != 1:
                                not_matched = True
                                break
                for li in range(n):
                    if not_matched:
                        break
                    for lj in range(n):
                        if lock_copied[li][lj] != 1:
                            not_matched = True
                            break
                if not not_matched:
                    return True
        return False

    if check(key, lock):
        return True
    for i in range(3):
        lock = rotate(lock)
        if check(key, lock):
            return True
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
ret = solution(key, lock)
print(ret)


