"""ver 1
def dfs(root, cur):
    if visited[cur]:
        return
    visited[cur] = True

    graph[root][cur] = 1
    for next in adj[cur]:
        dfs(root, next)


N,M = map(int, input().split())

adj = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)

graph = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    visited = [False] * (N+1)
    dfs(i, i)


in_degree = [0] * (N+1)
out_degree = [0] * (N+1)

for i in range(1, N+1):
    for j in range(1, N+1):
        if i != j and graph[i][j] == 1:
            in_degree[j] += 1
            out_degree[i] += 1

ans = 0
for i in range(1, N+1):
    if in_degree[i] + out_degree[i] == N - 1:
        ans += 1
print(ans)
"""

""" ver 2 """
INF = int(1e9)
N,M = map(int, input().split())

graph = [[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

for i in range(1, N+1):
    graph[i][i] = 1

for k in range(1, N+1):
#for k in range(0, N):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

in_degree = [0] * (N+1)
out_degree = [0] * (N+1)
for i in range(1, N+1):
    for j in range(1, N+1):
        if i != j and graph[i][j] < INF:
            in_degree[j] += 1
            out_degree[i] += 1

ans = 0
for i in range(1, N+1):
    if in_degree[i] + out_degree[i] == N - 1:
        ans += 1
print(ans)
