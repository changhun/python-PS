from collections import deque

def solution(food_times, k):
    food_enums = [[food_times[i], i + 1] for i in range(len(food_times))]
    # 이 부분이 핵심임. 이렇게 하면 O(1) 시간에 엔트리 하나를 제거 할 수 있음. 나중에 다시 x[1] 로 정렬하면 됨.
    #q.sort(key=lambda x:x[0]) # deque 는 sort 가 안됨
    q = deque(sorted(food_enums, key=lambda x: x[0]))
    # deque 는 sort() 함수가 안 되서 sorted 함수를 호출했는데 이는 list 를 리턴하는 것으로 보인다.

    eaten = 0
    for _ in range(len(food_times)):
        if (q[0][0] - eaten) * len(q) > k:
            break
        k -= (q[0][0] - eaten) * len(q)
        eaten = q[0][0]
        q.popleft()

    if len(q) == 0:
        return -1
    remain_foods = [q[i][1] for i in range(len(q))]
    remain_foods.sort()
    #return remain_foods[(k+1) % len(remain_foods)]
    return remain_foods[k % len(remain_foods)]


food_times = [3, 1, 2]
k = 5
ret = solution(food_times, k)
print(ret)

