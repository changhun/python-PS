before = input()
after = input()

n = len(before)
m = len(after)
dist = [[0] * m for _ in range(n)]

for i in range(m):
    dist[0][i] = i

for i in range(n):
    dist[i][0] = i

for i in range(1, n):
    for j in range(1, m):
        min_val = min(dist[i-1][j] + 1, dist[i][j-1] + 1)
        if before[i] == after[j]:
            min_val = min(min_val, dist[i-1][j-1])
        else:
            min_val = min(min_val, dist[i-1][j-1] + 1)
        dist[i][j] = min_val

print(dist[n-1][m-1])
