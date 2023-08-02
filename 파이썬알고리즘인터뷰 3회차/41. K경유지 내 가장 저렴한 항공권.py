import heapq
import collections

INF = int(1e9)
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        dist = [(INF, INF)] * (n+2)
        q = []

        adj = collections.defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))

        # dist, stops
        dist[src] = (0, 0)
        # dist, stops, here
        heapq.heappush(q, (0, 0, src))
        while q:
            distance, stops, here = heapq.heappop(q)
            if here == dst:
                return distance

            if dist[here][0] < distance and dist[here][1] <= stops:
                continue

            for there, cost in adj[here]:
                if there != dst and stops >= k:
                    continue
                if dist[there][0] <= distance + cost and dist[there][1] <= stops + 1:
                    continue
                if distance + cost < dist[there][0]:
                    dist[there] = (distance + cost, stops + 1)
                heapq.heappush(q, (distance + cost, stops + 1, there))

        return -1


n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1

ret = Solution().findCheapestPrice(n, flights, src, dst, k)
print(ret)
