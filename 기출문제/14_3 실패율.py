def solution(N, stages):
    answer = []
    stage_count = [0] * (N+2) # 0 ~ N+1
    for i in range(len(stages)):
        stage_count[stages[i]] += 1

    pSum = [0] * (N+2) # 0 ~ N + 1
    pSum[N+1] = stage_count[N+1]

    # N ~ 1
    for i in range(N, 0, -1):
        pSum[i] = pSum[i+1] + stage_count[i]

    fail_rate = []
    for i in range(1, N+1):
        # 분모가 0 이 되는 조건때문에 런타임 에러남!!!
        if pSum[i] != 0:
            fail_rate.append((i, stage_count[i] / pSum[i]))
        else:
            fail_rate.append((i, 0))

    fail_rate.sort(key=lambda x : (-x[1], x[0]))
    for i in range(N):
        answer.append(fail_rate[i][0])

    return answer


N = int(input())
stages = list(map(int, input().split(sep=',')))
ret = solution(N, stages)
print(ret)