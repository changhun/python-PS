import collections
from collections import deque


class Solution:
    answer = []
    def findItinerary(self, tickets:list[list[str]]):
        adj = collections.defaultdict(deque)
        degree = collections.defaultdict(int)
        path = []
        def dfs(here):
            # 루프 돌면서 deque 를 계속 변경(첫번째 item 삭제) 해야하므로 for 문 대신 while 문 사용 해야할듯!!!!
            #for there in adj[here]:
            q = adj[here]
            while q:
                there = q.popleft()
                dfs(there)
            path.append(here)

        for ticket in tickets:
            a, b = ticket[0], ticket[1]

            adj[a].append(b)
            degree[a] -= 1
            degree[b] += 1

        """
        for value in adj.values():
            #value.sort()
            #print(value)
            value = deque(sorted(value))
            #print(value)
        """

        for key in adj.keys():
            adj[key] = deque(sorted(adj[key]))
        u = "JFK"
        v = ""
        for key, value in degree.items():
            if value & 1 == 1:
                v = key

        adj[v].appendleft(u)
        # degree 는 굳이 추가하지 않겠다.

        dfs(v)
        path.reverse()
        return path[1:]


tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

ret = Solution().findItinerary(tickets)
print(ret)


