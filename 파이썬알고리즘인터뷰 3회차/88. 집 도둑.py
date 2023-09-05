from typing import List

MAX_SIZE = (100 + 2)


class Solution:
    dp = [-1] * MAX_SIZE

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        self.dp[0] = nums[0]
        self.dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            self.dp[i] = max(self.dp[i - 1], self.dp[i - 2] + nums[i])

        return self.dp[len(nums) - 1]


nums = [2,1]
ret = Solution().rob(nums)
print(ret)