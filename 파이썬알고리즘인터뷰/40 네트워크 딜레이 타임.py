
"""
1. heapq 사용법
2. 다익스트라 작성.
    - 루프 들어가기 전에 첫 노드의 distance 업데이트
    - 루프 전반에 pop 할 때 조건문: if distance[here] < dist: continue
    - there 을 큐에 넣을 때 조건문: if dist + cost < distance[there]:
3. adj 와 distance 에 리스트가 아닌 defaultdict 사용해보기
4. dict 에서 max 값 얻어내는 법 확인하기
"""
import collections
import heapq
import sys
INF = sys.maxsize

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        #distance = [INF]*n
        distance = {}
        for i in range(1, n+1):
            distance[i] = INF

        graph = collections.defaultdict(list)
        for time in times:
            a, b, cost = time[0], time[1], time[2]
            graph[a].append((b, cost))

        def dijkstra(start):
            #q = heapq((0, start))
            q = [(0, start)]
            heapq.heapify(q)
            distance[start] = 0

            while q:
                #dist, here = q.pop()
                dist, here = heapq.heappop(q)
                #if distance[here] != INF:
                if distance[here] < dist:
                    continue

                for there, cost in graph[here]:
                    if dist + cost < distance[there]:
                        distance[there] = dist + cost
                        heapq.heappush(q, (distance[there], there))

        dijkstra(k)
        for i in range(1, n+1):
            if distance[i] == INF:
                return -1
        max_val = max(distance.values())
        return max_val


times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
ret = Solution().networkDelayTime(times, n , k)
print(ret)