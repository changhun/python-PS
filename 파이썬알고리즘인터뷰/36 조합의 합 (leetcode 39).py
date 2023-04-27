MAX_TARGET = 40

class Solution:
    def combinationSum(self, candi: list[int], target: int) -> list[list[int]]:
        ans = []
        memo = [0] * (MAX_TARGET + 1)

        def dfs(cur_value, path, candi_index):
            if cur_value > target:
                return False
            elif cur_value == target:
                ans.append(path[:])

            if memo[cur_value] == -1:
                return False

            ret = False
            for i in range(candi_index, len(candi)):
                num = candi[i]
                path.append(num)
                if dfs(cur_value + num, path, i):
                    ret = True

                path.pop()

            if ret:
                memo[cur_value] = 1

            return ret

        path = []
        dfs(0, path, 0)
        return ans


candidates = [2,3,6,7]
target = 7

ret = Solution().combinationSum(candidates, target)
print(ret)