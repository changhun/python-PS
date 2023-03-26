def find_parent(a, parents):
    #while parents[a] != a:
    #    a = parents[a]
    if parents[a] != a:
        parents[a] = find_parent(parents[a], parents)

    return parents[a]


def union_parents(a, b, parents):
    pa = find_parent(a, parents)
    pb = find_parent(b, parents)
    if pa < pb:
        parents[pb] = pa
    else:
        parents[pa] = pb


N, M = map(int, input().split())
parents = [i for i in range(N+1)]
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            union_parents(i+1, j+1, parents)

places = list(map(int, input().split()))

ans = True
for i in range(1, M):
    if find_parent(places[i-1], parents) != find_parent(places[i], parents):
        ans = False
        break
if ans:
    print("YES")
else:
    print("NO")
