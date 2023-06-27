n, m = map(int, input().split())
adj = []
for i in range(m):
    a, b, c = map(int, input().split())
    adj.append((a, b, c))

parent = [i for i in range(n + 1)]


def get_parent(parent, a):
    if parent[a] == a:
        return a
    parent[a] = get_parent(parent, parent[a])
    return parent[a]


def union(parent, a, b):
    pa = get_parent(parent, a)
    pb = get_parent(parent, b)

    if pa > pb:
        pa, pb = pb, pa
    parent[pb] = pa


adj.sort(key=lambda x: x[2])
kruskal_edges = []
for a, b, c in adj:
    if get_parent(parent, a) == get_parent(parent, b):
        continue
    kruskal_edges.append(c)

ans = sum(kruskal_edges) - max(kruskal_edges)
print(ans)
