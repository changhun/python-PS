import sys
input = sys.stdin.readline


def is_ok(pos, C, min_dist):
    cur_idx, next_idx = 0, 1
    count = 1

    while count < C and next_idx < len(pos):
        if pos[next_idx] >= pos[cur_idx] + min_dist:
            cur_idx = next_idx
            count += 1
        next_idx += 1
    return count == C


# 이 함수는 pos 는 정렬된 값을 받는다.
def binary_search(pos, C):
    s, e = 1, pos[-1] - pos[0]
    ans = -1
    while s <= e:
        m = (s+e)//2
        if is_ok(pos, C, m):
            ans = m
            s = m + 1
        else:
            e = m - 1
    return ans


N, C = map(int, input().split())
pos = []
for _ in range(N):
    pos.append(int(input()))
pos.sort()
ret = binary_search(pos, C)
print(ret)

