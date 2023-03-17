
def check(key, lock):
    key_size = len(key)
    lock_size = len(lock)

    for sy in range(-key_size + 1, lock_size):
        for sx in range(-key_size + 1, lock_size):
            for ky in range(0, key_size):
                for kx in range(0, key_size):
                    ly = sy + ky
                    lx = sx + kx
                    if lx < 0 or lx >= lock_size:
                        continue
                    if ly < 0 or ly >= lock_size:
                        continue
                    lock[ly][lx] += key[ky][kx]

            invalid = False
            for ly in range(0, lock_size):
                if invalid:
                    break
                for lx in range(0, lock_size):
                    if lock[ly][lx] != 1:
                        invalid = True
                        break
            if not invalid:
                """
                print(sy, sx)
                for key_row in key:
                    print(key_row)
                """
                return True

            for ky in range(0, key_size):
                for kx in range(0, key_size):
                    ly = sy + ky
                    lx = sx + kx
                    if lx < 0 or lx >= lock_size:
                        continue
                    if ly < 0 or ly >= lock_size:
                        continue
                    lock[ly][lx] -= key[ky][kx]

    return False


def solution(key, lock):
    key_size = len(key)
    lock_size = len(lock)
    #next_key = [[key[i][j] for j in range(key_size) for i in range(key_size)]]
    next_key = key
    for _ in range(4):
        ret = check(next_key, lock)
        if (ret):
            return True
        prev = next_key
        next_key = [[prev[key_size - j - 1][i] for j in range(key_size)] for i in range(key_size)]

    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
ret = solution(key, lock)
print(ret)