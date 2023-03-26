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


N, M = map(int, input().split())
parents = [i for i in range(N+1)]
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

total_sum = 0
valid_val = 0
edges.sort()
for c, a, b in edges:
    if find_parent(a, parents) != find_parent(b, parents):
        union_parent(a, b, parents)
        valid_val += c
    total_sum += c

print(total_sum - valid_val)