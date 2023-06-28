import collections

n = int(input())

#adj = [] * (n+1)
adj = [[] for _ in range(n+1)]
indegree = [0] *(n+1)
prev_time = [0] * (n + 1)
course_time = [0] * (n + 1)
ans = [0] * (n + 1)


for i in range(1, n+1):
    row = list(map(int, input().split()))
    course_time[i] = row[0]

    for necessary_course in row[1:]:
        if necessary_course == -1:
            break
        try:
            adj[necessary_course].append(i)
        except IndexError:
            print(f"index error necessary_course: {necessary_course}")
        indegree[i] += 1

q = collections.deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
        ans[i] = course_time[i]

while q:
    here = q.popleft()
    for there in adj[here]:
        indegree[there] -= 1
        prev_time[there] = max(prev_time[there], ans[here])
        if indegree[there] == 0:
            ans[there] = prev_time[there] + course_time[there]
            q.append(there)

for taken in ans[1:]:
    print(taken)