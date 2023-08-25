import itertools

""" Using itertools
class Solution:
    def permute(self, l:list[int])->list[list[int]]:
        ans = itertools.permutations(l, len(l))
        return ans
"""

""" Using itertools """
class Solution:
    def permute(self, l:list[int])->list[list[int]]:
        ans = []
        permutation = []
        visited = [False]*len(l)
        def dfs(start):
            if start >= len(l):
                #ans.append(permutation)
                ans.append(permutation[:])

            for i in range(len(l)):
                if visited[i]:
                    continue
                permutation.append(l[i])
                visited[i] = True
                dfs(start+1)
                visited[i] = False
                permutation.pop()
        dfs(0)
        return ans

l = [1,2,3]
ret = Solution().permute(l)
print(ret)