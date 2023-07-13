from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_multi = [nums[0]]
        for num in nums[1:]:
            left_multi.append(left_multi[-1] * num)

        right_multi = [1]*len(nums)
        right_multi[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            right_multi[i] = right_multi[i+1] * nums[i]

        ans = [1] * len(nums)
        for i in range(len(nums)):
            if i - 1 >= 0:
                ans[i] *= left_multi[i-1]
            if i + 1 <= len(nums)-1:
                ans[i] *= right_multi[i+1]
        return ans


nums = [1,2,3,4]
nums = [-1, 1, 0, -3, 3]
ret = Solution().productExceptSelf(nums)
print(ret)
