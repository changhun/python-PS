import heapq
import collections
import sys

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        INF = sys.maxsize
        Q = []
        distance = {}
        for i in range(1, n+1):
            distance[i] = INF
        graph = collections.defaultdict(list)
        for a, b, c in times:
            graph[a].append((b, c))

        distance[k] = 0
        heapq.heappush(Q, (0, k))
        while Q:
            dist, here = heapq.heappop(Q)
            if distance[here] < dist:
                continue

            for next, cost in graph[here]:
                if dist + cost < distance[next]:
                    distance[next] = dist + cost
                    heapq.heappush(Q, (dist + cost, next))

        dist = max(distance.values())
        if dist >= INF:
            dist = -1
        return dist

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
ret = Solution().networkDelayTime(times, n, k)
print(ret)