INF = int(1e9)


def distance(chi_idx, home_idx, chicken_pos, home_pos):
    dist = abs(chicken_pos[chi_idx][0] - home_pos[home_idx][0]) + abs(chicken_pos[chi_idx][1] - home_pos[home_idx][1])
    return dist


def chicken_distance(chicken_list, dist):
    chicken_dist = 0
    chicken_nums = len(dist)
    home_nums = len(dist[0])
    chicken_dist = 0
    for home_idx in range(home_nums):
        min_dist = INF
        for j in range(len(chicken_list)):
            chicken_idx = chicken_list[j]
            min_dist = min(min_dist, dist[chicken_idx][home_idx])
        chicken_dist += min_dist
    return chicken_dist

ANS = INF


# def combination(start, remain, comb, dist):
#     if remain == 0:
#         ANS = min(ANS, chicken_distance(comb, dist))
#         return
#     chicken_nums = len(dist)
#     home_nums = len(dist[0])
#     if start >= chicken_nums:
#         return
#
#     for i in range(start, chicken_nums):
#         comb.append(remain)
#         # combination(start, remain-1, comb, dist) # 이부분이 잘 못 되어서 시간초과 되었음!!!
#         combination(i + 1, remain-1, comb, dist)
#         comb.pop()

def combination(start, remain, comb, dist):
    ret = INF
    if remain == 0:
        return chicken_distance(comb, dist)

    chicken_nums = len(dist)
    home_nums = len(dist[0])
    if start >= chicken_nums:
        return INF

    for i in range(start, chicken_nums):
        comb.append(i)
        ret = min(ret, combination(start, remain-1, comb, dist))
        comb.pop()
    return ret


n, m = map(int, input().split())
#board = []
#for i in range(n):
#    board.append(list(map(int, input().split())))

board = [0]*n
for i in range(n):
    board[i] = list(map(int, input().split()))

chicken_pos = []
home_pos = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            home_pos.append((i, j))
        elif board[i][j] == 2:
            chicken_pos.append((i, j))

dist = [[INF]*len(home_pos) for _ in range(len(chicken_pos))]
for i in range(len(chicken_pos)):
    for j in range(len(home_pos)):
        dist[i][j] = distance(i, j, chicken_pos, home_pos)


l = []
ret = combination(0, m, l, dist)
print(ret)


