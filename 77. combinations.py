class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:

        def dfs(start: int, remain_cnt: int):
            if n - start < remain_cnt:
                return
            if remain_cnt == 0:
                ans.append(path[:])
                return
            i = start
            while i < n:
                path.append(i+1)
                dfs(i+1, remain_cnt - 1)
                path.pop()
                i += 1

        ans = []
        path = []

        dfs(0, k)
        #print(ans)
        return ans


sol = Solution()
#n = 4, k = 2
n, k = 4, 2
sol.combine(n, k)
