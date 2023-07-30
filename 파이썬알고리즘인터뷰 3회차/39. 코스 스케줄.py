import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        indegree = [0] * numCourses
        adj = collections.defaultdict(list)
        for there, here in prerequisites:
            adj[here].append(there)
            indegree[there] += 1
        q = collections.deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        while q:
            here = q.popleft()
            for there in adj[here]:
                indegree[there] -= 1
                if indegree[there] == 0:
                    q.append(there)
        return indegree.count(0) == numCourses