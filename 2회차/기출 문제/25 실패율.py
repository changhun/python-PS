import sys
input = sys.stdin.readline


def solution(N, stages):
    stage_count = [0] * (N + 2)
    for i in range(1, N + 2):
        stage_count[i] = stages.count(i)

    # rate Vs. ratio 어떻게 다른지
    fail_ratio = []
    approach_count = sum(stage_count)
    #for i in range(1, N+2):
    for i in range(1, N + 1):
        if stage_count[i] == 0:
            fail_rate = 0
        else:
            fail_rate = stage_count[i]/approach_count
        approach_count -= stage_count[i]
        fail_ratio.append((fail_rate, i))


    fail_ratio.sort(key=lambda x: -x[0])
    ans = [fail_ratio[i][1] for i in range(N)]
    return ans


N = int(input())
stages = list(map(int, input().split(',')))
ret = solution(N, stages)
print(ret)
