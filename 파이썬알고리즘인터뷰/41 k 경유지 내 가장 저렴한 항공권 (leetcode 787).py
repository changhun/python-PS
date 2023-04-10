import collections
from collections import deque
import sys
INF = sys.maxsize


""" ver1"""
#timeout at 46/52
"""
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        distance = collections.defaultdict(int)
        for i in range(n):
            distance[i] = INF
        for flight in flights:
            a, b, cost = flight[0], flight[1], flight[2]
            graph[a].append((b, cost))
        q = deque()
        # here, stopover, dist
        q.append((src, -1, 0))
        distance[src] = 0
        while q:
            here, stopover, cur_dist = q.popleft()
            if stopover > k:
                break

            for there, cost in graph[here]:
                if stopover + 1 <= k and cur_dist + cost < distance[there]:
                    distance[there] = cur_dist + cost
                q.append((there, stopover+1, cur_dist + cost))

        if distance[dst] == INF:
            return -1
        return distance[dst]
"""
""" ver2 """
#timeout at 46/52
"""
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        distance = [[INF] * (n+1) for _ in range(n)]

        for flight in flights:
            a, b, cost = flight[0], flight[1], flight[2]
            graph[a].append((b, cost))
        q = deque()
        # here, stopover, dist
        q.append((src, 0, 0))
        distance[src][0] = 0
        while q:
            here, stopover, cur_dist = q.popleft()
            if stopover - 1 > k:
                break

            for there, cost in graph[here]:
                next_stopover = stopover + 1
                if next_stopover - 1 <= k and cur_dist + cost < distance[there][next_stopover]:
                    distance[there][next_stopover] = cur_dist + cost
                    q.append((there, next_stopover, cur_dist + cost))
        min_val = min(distance[dst])
        if min_val == INF:
            return -1
        return min_val
"""


""" ver3 """
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        distance = [[INF] * (n+2) for _ in range(n)]

        for flight in flights:
            a, b, cost = flight[0], flight[1], flight[2]
            graph[a].append((b, cost))

        q = []
        # dist, here, stopover
        heapq.heappush(q, (0, src, 0))

        # here, stopover, dist
        distance[src][0] = 0
        while q:
            cur_dist, here, stopover = heapq.heappop(q)
            #if stopover - 1 > k:
            #    break

            # try:
            #     if distance[here][stopover] < cur_dist:
            #         continue
            # except IndexError:
            #     print(here, stopover)

            if distance[here][stopover] < cur_dist:
                continue

            for there, cost in graph[here]:
                next_stopover = stopover + 1
                if next_stopover - 1 <= k and cur_dist + cost < distance[there][next_stopover]:
                    distance[there][next_stopover] = cur_dist + cost
                    heapq.heappush(q, (cur_dist + cost, there, next_stopover))
        min_val = min(distance[dst])
        if min_val == INF:
            return -1
        return min_val

flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
n, k, src, dst = 4, 1, 0, 3
ret = Solution().findCheapestPrice(n, flights, src, dst, k)
print(ret)