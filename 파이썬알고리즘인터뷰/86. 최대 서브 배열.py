from typing import List
import sys


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -sys.maxsize
        total = 0
        for i, num in enumerate(nums):
            total += num
            ans = max(ans, total)
            if total < 0:
                total = 0

        return ans


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
ret = Solution().maxSubArray(nums)
print(ret)