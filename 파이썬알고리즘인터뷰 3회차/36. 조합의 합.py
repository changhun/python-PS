class Solution:
    def combinationSum(self, candi: list[int], target: int) -> list[list[int]]:
        def dfs(si: int, sub_target: int, comb: list[int]):
            if sub_target == 0:
                return ans.append(comb[:])
            if sub_target < 0:
                return
            
            ret = 0
            for i in range(si, len(candi)):
                comb.append(candi[i])
                dfs(i, sub_target - candi[i], comb)
                comb.pop()

        ans = []

        dfs(0, target, [])
        return ans

candidates =[2,3,6,7]
target = 7
ret = Solution().combinationSum(candidates, target)
print(ret)