from collections import deque

def solution(food_times, k):
    q = deque()
    for i in range(len(food_times)):
        q.append((food_times[i], i + 1))
    q = deque(sorted(q))

    i = 0
    length = len(q)
    eaten = 0
    while i < length:
        if len(q) * (q[0][0] - eaten) > k:
            break
        k -= len(q) * (q[0][0] - eaten)

        eaten = q[0][0]
        q.popleft()

        i += 1

    if i == length:
        return -1

    q = sorted(q, key=lambda x: x[1])
    return q[k % len(q)][1]


food_times = [3, 6, 8, 10]
k = 23
ret = solution(food_times, k)
print(ret)
