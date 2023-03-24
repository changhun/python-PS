import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # 이거 안 하면 시간 초과됨.

N, L, R = map(int, input().split())
can_move = True
day = 0
population = []
for i in range(N):
    population.append(list(map(int, input().split())))

# 오른쪽, 아래쪽 두군데만 확인하기. 이렇게 하면 안된다!!!! 정리하기!!!
# => (0,0) -> (0, 1) -> (1, 1) -> (1, 0) 이렇게 오른쪽 하단에서 왼쪽 하단으로 오는 시나리오도 있다.
#dy = [0, 1]
#dx = [1, 0]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def dfs(population, ally_number, ally_size, ally_sum, ally_count, y, x):
    if ally_number[y][x] != -1:
        return
    ally_number[y][x] = ally_count
    ally_size[ally_count] += 1
    ally_sum[ally_count] += population[y][x]
    for di in range(4):
        ny = y + dy[di]
        nx = x + dx[di]
        if ny >= N or nx >= N or ny < 0 or nx < 0:
            continue
        if L <= abs(population[y][x] - population[ny][nx]) <= R:
            dfs(population, ally_number, ally_size, ally_sum, ally_count, ny, nx)


while can_move:
    ally_size = [0] * (N*N)
    ally_sum = [0] * (N*N)
    ally_number = [[-1]*N for _ in range(N)]
    ally_count = 0

    for i in range(N):
        for j in range(N):
            if ally_number[i][j] != -1:
                continue
            #ally_number[i][j] = ally_count
            dfs(population, ally_number, ally_size, ally_sum, ally_count, i, j)
            ally_count += 1

    if ally_count < N*N:
        can_move = True
        day += 1
        ally_avg = [ally_sum[i] // ally_size[i] for i in range(ally_count)]

        for i in range(N):
            for j in range(N):
                population[i][j] = ally_avg[ally_number[i][j]]

    else:
        can_move = False

print(day)
