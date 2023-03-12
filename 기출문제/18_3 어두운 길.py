def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def unite(parent, a, b):
    pa = find_parent(parent, a)
    pb = find_parent(parent, b)

    if pa == pb:
        return False

    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb
    return True


N, M = map(int, input().split())
parent = [i for i in range(N+1)]

#edge_sum = 0
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
#    edge_sum += c
#print(edge_sum)


ans = 0
edges.sort(key=lambda x: x[0])
for c, a, b in edges:
    if find_parent(parent, a) == find_parent(parent, b):
        ans += c
        continue
    unite(parent, a, b)

print(ans)