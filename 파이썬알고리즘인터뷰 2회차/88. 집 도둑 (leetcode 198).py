from typing import List
MAX_SIZE = (100 + 2)

class Solution:
    dp = [-1] * MAX_SIZE
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        self.dp[n-1] = nums[n-1]
        self.dp[n-2] = max(self.dp[n-1], nums[n-2])
        for i in range(n-3, -1, -1):
            self.dp[i] = max(nums[i] + self.dp[i+2], self.dp[i +1])

        return self.dp[0]



nums = [1,2,3,1]
nums = [2,7,9,3,1]
ret = Solution().rob(nums)
print(ret)