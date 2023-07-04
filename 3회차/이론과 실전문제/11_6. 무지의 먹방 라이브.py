import collections


def solution(food_times, k):
    food_times_with_idx = collections.deque([[i, time] for i, time in enumerate(food_times)])

    #food_times_with_idx = collections.deque(food_times_with_idx.sort(key = lambda x: x[1]))
    food_times_with_idx = collections.deque(sorted(food_times_with_idx, key=lambda x: x[1]))

    eaten = 0
    while food_times_with_idx and k >= len(food_times_with_idx) * (food_times_with_idx[0][1] - eaten):
        k -= len(food_times_with_idx) * (food_times_with_idx[0][1] - eaten)
        eaten = food_times_with_idx[0][1]
        food_times_with_idx.popleft()

    if not food_times_with_idx:
        return -1

    food_times_with_idx = sorted(food_times_with_idx, key=lambda x : x[0])
    ans = food_times_with_idx[k % len(food_times_with_idx)][0] + 1
    return ans



food_times = [3, 1, 2]
k = 5

ret = solution(food_times, k)
print(ret)
