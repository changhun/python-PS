from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sequent_sums_from_index = [0] * n
        for i in range(n-1, -1, -1):
            if i < n-1 and max_sequent_sums_from_index[i+1] > 0:
                max_sequent_sums_from_index[i] = max_sequent_sums_from_index[i+1] + nums[i]
            else:
                max_sequent_sums_from_index[i] = nums[i]

        return max(max_sequent_sums_from_index)

nums = [5,4,-1,7,8]
ret = Solution().maxSubArray(nums)
print(ret)