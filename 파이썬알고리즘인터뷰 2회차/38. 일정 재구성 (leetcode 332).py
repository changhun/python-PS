import collections
from collections import deque


class Solution:
    answer = []
    def findItinerary(self, tickets:list[list[str]]):
        tickets.sort()
        graph = collections.defaultdict(deque)
        for src, dst in tickets:
            graph[src].append(dst)

        ans = []

        def dfs(cur):
            while graph[cur]:
                next = graph[cur].popleft()
                dfs(next)

            ans.append(cur)

        dfs("JFK")
        return list(reversed(ans))

tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
ret = Solution().findItinerary(tickets)
print(ret)