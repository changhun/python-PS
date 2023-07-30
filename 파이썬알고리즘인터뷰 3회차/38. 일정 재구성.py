import heapq
import collections

class Solution:
    answer = []
    def findItinerary(self, tickets:list[list[str]]):
        path = []
        adj = collections.defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(adj[src], dst)

        def dfs(here):
            while adj[here]:
                there = heapq.heappop(adj[here])
                dfs(there)
            path.append(here)

        dfs("JFK")
        path.reverse()
        return path


tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
ret = Solution().findItinerary(tickets)
print(ret)