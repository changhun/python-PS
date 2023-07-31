import heapq
import collections

INF = int(1e9)

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        dist = [INF] * (n+1)
        adj = collections.defaultdict(list)
        for source, destination, cost in times:
            adj[source].append((destination, cost))

        dist[k] = 0
        q = []
        heapq.heappush(q, (0, k))
        while q:
            distance, here = heapq.heappop(q)
            if distance > dist[here]:
                continue

            for there, cost in adj[here]:
                if distance + cost < dist[there]:
                    dist[there] = distance + cost
                    heapq.heappush(q, (dist[there], there))

        ans = max(dist[1:])
        if ans == INF:
            ans = -1
        return ans



times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
ret = Solution().networkDelayTime(times, n, k)
print(ret)
