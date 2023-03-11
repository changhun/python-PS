INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n + 1)]
for a in range(n+1):
    graph[a][a] = 0


for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

ans = 0
for person in range(1, n+1):
    access_cnt = 0
    for i in range(1, n+1):
        if person == i:
            continue
        if graph[person][i] < INF:
            access_cnt += 1
        elif graph[i][person] < INF:
            access_cnt += 1

    if access_cnt == n-1:
        ans += 1

print(ans)