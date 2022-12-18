from collections import deque

# arr = [[1,1], [2,2], [3,3], [4,4]]
# arr = deque([[1,1], [2,2], [3,3], [4,4]])
# print(arr)
# for i in range(4):
#     print(arr[i][0])
#     arr[i][0] -= 1
#     print(arr[i][0])
# print(arr)



def solution(food_times, k):
    q = deque()
    for i in range(len(food_times)):
        q.append([food_times[i], i + 1])
    #q.sort() # deque 는 sort 가 없나?
    q = deque(sorted(q))
    #print(q)

    i = 0
    length = len(q)
    eaten = 0
    while i < length:
        if len(q) * (q[0][0] - eaten)> k:
            break
        k -= len(q) * (q[0][0] - eaten)
        eaten = q[0][0]

        # 이렇게 하면 시간초과 나옴
        # for j in range(1, len(q)):
        #     q[j][0] -= q[0][0]

        q.popleft()

        i += 1

    if i == length:
        return -1

    q = sorted(q, key=lambda x: x[1])
    print(q)
    return q[(k) % len(q)][1]


# food_times = [3, 6, 8, 10]
# k = 23
food_times = [3, 1, 2]
k = 4
ret = solution(food_times, k)
print(ret)
