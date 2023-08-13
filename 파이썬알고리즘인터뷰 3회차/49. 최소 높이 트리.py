import collections

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        adj = collections.defaultdict(list)
        degree = [0] * (n)
        used = []
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1

        ans = []
        dist = -1
        #q = collections.deque()
        q = collections.deque([(i, 0) for i in range(n) if degree[i] == 1])

        while q:
            here, distance = q.popleft()
            if dist != distance:
                dist = distance
                if n - 1 == len(used) or len(used) == n - 2:
                    break

            degree[here] -= 1 # it should be 0
            used.append(here)
            for there in adj[here]:
                if degree[there] == 0:
                    continue
                degree[there] -= 1
                if degree[there] == 1:
                    q.append((there, distance + 1))


        ans = set([i for i in range(n)]) - set(used)
        ans = list(ans)


        return ans


n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
ret = Solution().findMinHeightTrees(n, edges)
print(ret)