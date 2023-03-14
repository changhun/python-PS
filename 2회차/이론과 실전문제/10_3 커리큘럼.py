from collections import deque
import sys
input = sys.stdin.readline


N = int(input())
#graph = []*(N+1)
graph = [[] for _ in range(N+1)]
cost = [0]*(N+1)
in_degrees = [0] * (N+1)
for target in range(1, N+1):
    data = list(map(int, input().split()))
    cost[target] = data[0]

    # 아래처럼 하면 data[1] ~ data[len(data)-2] 만큼 루프 도나? 마지막 entry 는 -1 이라서 무시하면 됨.
    for source in data[1:-1]:
        in_degrees[target] += 1
        graph[source].append(target)

total_costs = [0] * (N+1)

q = deque()
for i in range(1, N+1):
    if in_degrees[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    total_costs[cur] += cost[cur]

    for there in graph[cur]:
        # there 의 선수과목 코스중 가장 긴 코스 시간을 넣어둔다. 나중에 큐에서 there을 pop 할 때 there 의 선수과목 시간 + 자기 시간 한다.
        total_costs[there] = max(total_costs[there], total_costs[cur])
        in_degrees[there] -= 1
        if in_degrees[there] == 0:
            q.append(there)

for i in range(1, N+1):
    print(total_costs[i])