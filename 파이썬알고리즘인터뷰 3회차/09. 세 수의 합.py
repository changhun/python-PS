from typing import List

""" sol1: using two pointer """
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        for i in range(n-2):
            if i != 0 and nums[i-1] == nums[i]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j-1] == nums[j]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                    while j < k and nums[j-1] == nums[j]:
                        j += 1
                else:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return ans


nums = [-1,0,1,2,-1,-4]
ans = Solution().threeSum(nums)
print(ans)
