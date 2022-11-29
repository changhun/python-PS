from collections import deque

n = int(input())
result = [0] * (n+1)

indegree = [0] * (n + 1)
graph = [[] for _ in range(n+1)]

time = [0]
for b in range(1, n+1):
    input_row = list(map(int, input().split()))
    time.append(input_row[0])
    for a in input_row[1: -1]:
        graph[a].append(b)
        indegree[b] += 1

def topology_sort():
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        here = q.popleft()
        result[here] += time[here]

        for there in graph[here]:
            indegree[there] -= 1
            result[there] = max(result[there], result[here])
            if indegree[there] == 0:
                q.append(there)


topology_sort()

for i in range(1, n+1):
    print(result[i])


"""    
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""