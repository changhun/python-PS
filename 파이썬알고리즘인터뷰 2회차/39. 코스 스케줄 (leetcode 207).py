from collections import deque

"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        topology_list = []

        graph = [[] for _ in range(numCourses)]
        in_degrees = [0] * numCourses
        for a, b in prerequisites:
            graph[a].append(b)
            in_degrees[b] += 1


        q = deque()
        for i, in_degree in enumerate(in_degrees):
            if in_degree == 0:
                q.append(i)

        while q:
            here = q.popleft()
            topology_list.append(here)
            for next in graph[here]:
                in_degrees[next] -= 1
                if in_degrees[next] == 0:
                    q.append(next)

        return len(topology_list) == numCourses
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        visited = [False] * numCourses
        finished = [False] * numCourses

        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)

        def dfs(here):
            visited[here] = True
            for next in graph[here]:
                if visited[next] and not finished[next]:
                    return False
                if not visited[next]:
                    if not dfs(next):
                        return False

            finished[here] = True
            return True

        for i in range(numCourses):
            if not visited[i]:
                if not dfs(i):
                    return False
        return True


numCourses = 2
prerequisites = [[1,0],[0,1]]
ret = Solution().canFinish(numCourses, prerequisites)
print(ret)