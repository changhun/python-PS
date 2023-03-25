# combination Vs. permutation 사용법
# 배열 두개 일때 루프 어떤 거 기준으로 돌지
# 변수 이름 헷갈리지 않게. weak Vs. weak_copy


from itertools import combinations, permutations
INF = int(1e9)


def can_cover(n, weak_copy, dist_comb, weak_start):
    weak_len = len(weak_copy)//2
    cur_idx = weak_start
    next_idx = cur_idx + 1
    count = 1

    dist_idx = 0
    #while dist_idx < len(dist_comb) and count < weak_len and next_idx < len(weak_copy):
    #while dist_idx < len(dist_comb) and count < weak_len and next_idx < weak_start + weak_len:
    while dist_idx < len(dist_comb) and count < weak_len:
        if weak_copy[next_idx] <= weak_copy[cur_idx] + dist_comb[dist_idx]:
            count += 1
            next_idx += 1
        else:
            cur_idx = next_idx
            next_idx += 1
            dist_idx += 1
            if dist_idx < len(dist_comb):
                count += 1 # 이렇게 하는게 맞나? dist_idx 가 남아 있을 때만 추가해야할듯. 아니면 앞쪽에(while 바로 다음) 작성하던가

    return count == weak_len


def can_cover_ver2(n, weak_copy, dist_comb, weak_start):
    weak_len = len(weak_copy)//2
    cur_idx = weak_start
    next_idx = cur_idx + 1
    count = 0

    for dist_idx in range(len(dist_comb)):
        count += 1
        while next_idx < weak_start + weak_len and weak_copy[next_idx] <= weak_copy[cur_idx] + dist_comb[dist_idx]:
            count += 1
            next_idx += 1
        cur_idx = next_idx
        next_idx += 1
        #if next_idx >= weak_start + weak_len:
        if count >= weak_len:
            return True

    return False


def can_cover_ver3(n, weak_copy, dist_comb, weak_start):
    weak_len = len(weak_copy)//2

    dist_idx = 0
    prev_cover = weak_copy[weak_start] + dist_comb[0]
    for weak_idx in range(weak_start, weak_start + weak_len):
        if weak_copy[weak_idx] > prev_cover:
            if dist_idx == len(dist_comb) - 1:
                return False

            dist_idx += 1
            prev_cover = weak_copy[weak_idx] + dist_comb[dist_idx]

    return True


def inspect(n, weak_copy, dist_comb):
    weak_len = len(weak_copy)//2
    for i in range(weak_len):
        if can_cover_ver3(n, weak_copy, dist_comb, i):
            return True
    return False


def solution(n, weak, dist):
    weak_copy = [w for w in weak]
    for w in weak:
        weak_copy.append(w + n)

    dist.sort()

    for min_person in range(1, len(dist) + 1):
        #dist_combs = combinations(dist[len(dist)-min_person:], min_person)
        dist_combs = permutations(dist[len(dist) - min_person:], min_person)
        for dist_comb in dist_combs:
            ret = inspect(n, weak_copy, dist_comb)
            if ret is True:
                return min_person
    return -1


n = int(input())
weak = list(map(int, input().split(sep=',')))
dist = list(map(int, input().split(sep=',')))
ans = solution(n, weak, dist)
print(ans)

