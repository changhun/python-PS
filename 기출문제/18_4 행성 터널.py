# 백준 사이트에서는 입력을 input 으로 받으니 시간초과됨. sys.stdin.readline 으로 변경하니 통과됨.

import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(input())
parent = [i for i in range(N)]

#"""
planets = []
for i in range(N):
    x, y, z = map(int, input().split())
    planets.append((x, y, z, i))

edges = []
for sort_index in range(3):
    planets.sort(key=lambda x: x[sort_index])
    for i in range(N - 1):
        x1, y1, z1, node_a = planets[i]
        x2, y2, z2, node_b = planets[i+1]
        edges.append((abs(planets[i+1][sort_index] - planets[i][sort_index]), planets[i][3], planets[i+1][3]))
#"""

"""
x_sort = []
y_sort = []
z_sort = []
for i in range(N):
    x, y, z = map(int, input().split())
    x_sort.append((x, i))
    y_sort.append((y, i))
    z_sort.append((z, i))

x_sort.sort()
y_sort.sort()
z_sort.sort()

edges = []
for i in range(N-1):
    edges.append((abs(x_sort[i][0] - x_sort[i+1][0]), x_sort[i][1], x_sort[i+1][1]))
    edges.append((abs(y_sort[i][0] - y_sort[i + 1][0]), y_sort[i][1], y_sort[i + 1][1]))
    edges.append((abs(z_sort[i][0] - z_sort[i + 1][0]), z_sort[i][1], z_sort[i + 1][1]))
"""

edges.sort()
ans = 0
for c, a, b in edges:
    if find_parent(parent, a) == find_parent(parent, b):
        continue
    union_parent(parent, a, b)
    ans += c

print(ans)
