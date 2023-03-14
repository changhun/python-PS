import sys
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    pa = find_parent(parent, a)
    pb = find_parent(parent, b)
    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb


N, M = map(int, input().split())
parent = [i for i in range(N+1)]
edges = []
for i in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()
ans = 0
max_dist = 0
for c, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        ans += c
        max_dist = c

ans -= max_dist
print(ans)