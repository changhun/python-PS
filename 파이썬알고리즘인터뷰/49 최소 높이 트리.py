import sys
from collections import deque
from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        min_height = sys.maxsize
        height = [-1] * n
        for i in range(n):
            height[i] = self.get_height(i, graph, n)
            min_height = min(min_height, height[i])

        ans = []
        for i in range(n):
            if height[i] == min_height:
                ans.append(i)
        return ans


    def get_height(self, start, graph, n):
        distance = [-1] * n
        distance[start] = 0
        q = deque([start])

        while q:
            here = q.pop()

            for there in graph[here]:
                if distance[there] == -1:
                    distance[there] = distance[here] + 1
                    q.append(there)

        return max(distance)


edges = [[1,0],[1,2],[1,3]]
ret = Solution().findMinHeightTrees(4, edges)
print(ret)
