""" ver1: using combinations
from itertools import combinations

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        for i in range(len(nums) + 1):
            #ans += combinations(nums, i)
            for comb in combinations(nums, i):
                ans.append(list(comb))

        return ans
"""

""" ver2: dfs 
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        comb = []
        def dfs(here, cnt, comb_size):
            if cnt >= comb_size:
                ans.append(comb[:])
                return
            if here >= len(nums):
                return

            for i in range(here, len(nums)):
                comb.append(nums[i])
                dfs(i+1, cnt + 1, comb_size)
                comb.pop()

        for i in range(len(nums) + 1):
            dfs(0, 0, i)

        return ans
"""

""" ver3: dfs """
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        comb = []

        def dfs(here, cnt, comb_size):
            if cnt >= comb_size:
                ans.append(comb[:])
                return
            if here >= len(nums):
                return

            comb.append(nums[here])
            dfs(here + 1, cnt+1, comb_size)
            comb.pop()

            dfs(here + 1, cnt, comb_size)

        for i in range(len(nums) + 1):
            dfs(0, 0, i)

        return ans

nums = [1, 2, 3]
ret = Solution().subsets(nums)
print(ret)
