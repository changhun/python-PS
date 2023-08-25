from typing import List

"""sol1 """
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        MAX_NUM = 100
        memo = [-1] * (MAX_NUM + 2)

        if len(nums) <= 2:
            return max(nums)

        # 아래 부분 틀렸다!!! 풀어야 하는 문제가 무엇인지 생각하면서 작성하기
        memo[0] = nums[0]
        #memo[1] = nums[1]
        memo[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            memo[i] = max(memo[i-1], memo[i-2] + nums[i])

        return memo[len(nums) - 1]
"""

""" sol2: recursive """
MAX_NUM = 100
class Solution:
    def rob(self, nums: List[int]) -> int:
        def memoization(start):
            if start < 0:
                return 0

            if memo[start] != -1:
                return memo[start]

            memo[start] = max(memoization(start - 1), memoization(start - 2) + nums[start])
            return memo[start]

        memo = [-1] * (MAX_NUM + 2)
        memoization(len(nums) - 1)
        return memo[len(nums) - 1]

nums = [1,2,3,1]
nums = [2,7,9,3,1]
nums = [2,1,1,2]
ret = Solution().rob(nums)
print(ret)
