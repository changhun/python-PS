import heapq

n = int(input())

hp = [1]
heapq.heapify(hp)

prev = 0
for i in range(n):
    while prev == hp[0]:
        heapq.heappop(hp)
    prev = heapq.heappop(hp)
    heapq.heappush(hp, prev * 2)
    heapq.heappush(hp, prev * 3)
    heapq.heappush(hp, prev * 5)

print(prev)