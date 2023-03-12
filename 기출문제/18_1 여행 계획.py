import sys
input = sys.stdin.readline


def dfs(start, graph, visited):
    if visited[start]:
        return
    visited[start] = True

    for i in range(N):
        if graph[start][i] == 1:
            dfs(start)


N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
schedule = list(map(int, input().split()))
for val in schedule:
    val -= 1

visited = [False] * N
dfs(schedule[0], graph, visited)

if False in visited:
    print("NO")
else
    print("YES")