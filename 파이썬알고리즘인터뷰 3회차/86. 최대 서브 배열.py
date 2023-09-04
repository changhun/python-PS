from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum_till_now = nums[:]
        for i in range(1, len(nums)):
            if max_sum_till_now[i-1] > 0:
                max_sum_till_now[i] += max_sum_till_now[i-1]
        return max(max_sum_till_now)
