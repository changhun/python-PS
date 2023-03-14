import sys
input = sys.stdin.readline


N = int(input())
fear = list(map(int, input().split()))
fear.sort()

group_cnt = 0
start_idx = 0
while start_idx < N:
    max_fear = fear[start_idx]
    member_cnt = 1
    while member_cnt < max_fear and start_idx + member_cnt < N:
        max_fear = fear[start_idx + member_cnt]
        member_cnt += 1
    if member_cnt == max_fear:
        group_cnt += 1
    start_idx += member_cnt

print(group_cnt)