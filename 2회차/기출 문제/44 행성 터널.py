import sys
input = sys.stdin.readline
INF = int(1e9)

def find_parent(a, parents):
    if a != parents[a]:
        parents[a] = find_parent(parents[a], parents)
    return parents[a]


def union_parent(a, b, parents):
    pa = find_parent(a, parents)
    pb = find_parent(b, parents)
    if pa < pb:
        parents[pb] = pa
    else:
        parents[pa] = pb


n = int(input())
pos = []
for _ in range(n):
    pos.append(list(map(int, input().split())))

edges = []
for i in range(n-1):
    for j in range(i+1,n):
        cost = INF
        for k in range(3):
            cost = min(cost, abs(pos[i][k] - pos[j][k]))
        edges.append((cost, i, j))

parents = [i for i in range(n+1)]
edges.sort()
result = 0
for c, a, b in edges:
    if find_parent(a, parents) != find_parent(b, parents):
        result += c
        union_parent(a, b, parents)

print(result)