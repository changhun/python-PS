from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i


def find_parent(parent, x) -> int:
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

result = 0
largest_cost = 0
for cost, a, b in edges:
    pa = find_parent(parent, a)
    pb = find_parent(parent, b)
    if pa == pb:
        continue
    union(parent, pa, pb)
    result += cost
    largest_cost = cost

result -= largest_cost
print(result)


""" input
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
"""