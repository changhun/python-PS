from itertools import combinations

HOME = 1
CHICKEN = 2
INF = int(1e9)

def get_city_chicken_dist(homes, chickens):
    city_chicken_dist = 0
    # 아래 for문을 for hy, hx in homes: 로 수정하는게 나을 것 같다.
    for home in homes:
        chicken_dist = INF
        # 아래 for문을 for cy, cx in chickens: 로 수정하는게 나을 것 같다.
        for chicken in chickens:
            dist = abs(home[0] - chicken[0]) + abs(home[1] - chicken[1])
            chicken_dist = min(chicken_dist, dist)
        city_chicken_dist += chicken_dist
    return city_chicken_dist


N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

homes = []
chickens = []
for i in range(N):
    for j in range(N):
        if board[i][j] == HOME:
            homes.append((i, j))
        elif board[i][j] == CHICKEN:
            chickens.append((i, j))

ans = INF
chicken_combs = combinations(chickens, M)
for chicken_comb in chicken_combs:
    ans = min(ans, get_city_chicken_dist(homes, chicken_comb))

print(ans)
