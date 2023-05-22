import collections

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def max_depth(root: int) -> (int, int):
            visited[root] = True
            max_depth_child = -1
            max_sub_depth = 0
            max_end_node = -1;

            for next in graph[root]:
                if visited[next]:
                    continue
                depth, end_node = max_depth(next)
                if depth > max_sub_depth:
                    max_sub_depth = depth
                    max_depth_child = next
                    max_end_node = end_node

            if max_end_node == -1:
                max_end_node = root
            next_node[root] = max_depth_child
            return max_sub_depth + 1, max_end_node

        next_node = [-1] * n
        visited = [False] * n

        depth, start_node = max_depth(0)
        next_node = [-1] * n
        visited = [False] * n

        depth, end_node = max_depth(start_node)
        half = (depth+1) >> 1
        cur = start_node
        for i in range(half-1):
            cur = next_node[cur]

        ans = [cur]
        if depth & 1 == 0:
            ans.append(next_node[cur])

        return ans


n = 4
edges = [[1,0],[1,2],[1,3]]
n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]

ret = Solution().findMinHeightTrees(n, edges)
print(ret)