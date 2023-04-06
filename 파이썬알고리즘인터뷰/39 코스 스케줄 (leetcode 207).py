
""" dfs 로 싸이클이 있는지 보고 """
"""
    class Solution:
        def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
    
            def dfs(here):
                seqs[here] = seq[0]
                seq[0] += 1
    
                for there in graph[here]:
                    if seqs[there] == -1:
                        cycle = dfs(there)
                        if cycle:
                            return True
                    # seq 비교할 때 = 조건도 포함해야 자기자신으로 가는 싸이클도 검출할 수 있다.
                    if not finished[there] and seqs[there] <= seqs[here]:
                        return True
                finished[here] = True
    
            graph = [[] for _ in range(numCourses+1)]
            seqs = [-1] * (numCourses + 1)
            seq = [0]
            finished = [False] * (numCourses+1)
            for item in prerequisites:
                a, b = item[1], item[0]
                # 자기가 자기한테 가는것도 cycle 로 봄. 아래 예외처리 없으면 자기 node 로 가는 cycle 검출 못 해?
                # 위에서 seq 비교할 때 here, there 의 seq 가 같은 경우에도 싸이클로 보도록 하면 아래 예외처리는 필요없다.
                #if a == b:
                #    return False
                graph[a].append(b)
    
            for i in range(numCourses):
                if seqs[i] == -1:
                    cycle = dfs(i)
                    if cycle:
                        return False
    
            return True
"""

""" 아래 조건으로도 cycle 검출 할 수 있음. there 에 dfs 호출하기 전에 visited and not finished 이면 cycle 이 있다고 본다. """
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        def dfs(here):
            seqs[here] = seq[0]
            seq[0] += 1

            for there in graph[here]:
                if seqs[there] != -1 and not finished[there]:
                    return True
                if seqs[there] == -1:
                    cycle = dfs(there)
                    if cycle:
                        return True

                if not finished[there] and seqs[there] < seqs[here]:
                    return True
            finished[here] = True

        graph = [[] for _ in range(numCourses+1)]
        seqs = [-1] * (numCourses + 1)
        seq = [0]
        finished = [False] * (numCourses+1)
        for item in prerequisites:
            a, b = item[1], item[0]
            # dfs 를 위처럼 구현하였을 경우 자기자신으로 가는 cycle 도 검출됨.
            #if a == b:
            #    return False
            graph[a].append(b)

        for i in range(numCourses):
            if seqs[i] == -1:
                cycle = dfs(i)
                if cycle:
                    return False

        return True
"""

""" 위상 정렬 """
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses + 1)]
        in_degree = [0] * numCourses
        for item in prerequisites:
            a, b = item[1], item[0]
            # 자기가 자기한테 가는것도 cycle 로 봄. 아래 예외처리 없으면 자기 node 로 가는 cycle 검출 못 해?
            in_degree[b] += 1
            graph[a].append(b)

        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)

        while q:
            here = q.popleft()
            for there in graph[here]:
                in_degree[there] -= 1
                if in_degree[there] == 0:
                    q.append(there)

        # 접근되지않은 노드가 있으면 싸이클이 있는 것임
        for degree in in_degree:
            if degree != 0:
                return False
        return True

pre = [[1,0]]
numCourses = 2

pre = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
numCourses = 20


ret = Solution().canFinish(numCourses, pre)
print(ret)