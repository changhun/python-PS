CMD_UNION = 0
CMD_IS_GROUP = 1

n, m = map(int, input().split())

parent = [i for i in range(n+1)]


def get_parent(a):
    global parent
    if parent[a] == a:
        return a

    parent[a] = get_parent(parent[a])
    return parent[a]


def union(a, b):
    global parent
    pa = get_parent(a)
    pb = get_parent(b)
    if pa == pb:
        return
    if pa > pb:
        pa, pb = pb, pa
    parent[pb] = pa


for i in range(m):
    cmd, a, b = map(int, input().split())
    if cmd == CMD_UNION:
        union(a, b)
    else:
        if get_parent(a) == get_parent(b):
            print("YES")
        else:
            print("NO")