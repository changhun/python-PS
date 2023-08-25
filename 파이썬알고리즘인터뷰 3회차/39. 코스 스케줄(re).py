import collections

NOCYCLE = 0
CYCLE = 1


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        visited = [False] * numCourses
        finished = [False] * numCourses
        adj = collections.defaultdict(list)
        for there, here in prerequisites:
            adj[here].append(there)

        def dfs(here):
            visited[here] = True
            for there in adj[here]:
                if not visited[there]:
                    ret = dfs(there)
                    if ret == CYCLE:
                        return ret
                elif not finished[there]:
                    return CYCLE

            finished[here] = True
            return NOCYCLE

        for course in range(numCourses):
            if not visited[course]:
                ret = dfs(course)
                # if there's a cycle, it's not possible to finish all the courses.
                if ret == CYCLE:
                    return False
        return True