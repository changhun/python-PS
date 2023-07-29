class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        path = []
        def dfs(si: int, path: list[int], remains: int):
            ans.append(path[:])
            if si >= len(nums):
                return

            for i in range(si, len(nums)):
                path.append(nums[i])
                dfs(i+1, path, remains-1)
                path.pop()

        dfs(0, path, len(nums))
        return ans