from typing import List

""" sol1: using two pointer """
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        i = 0
        while i <= n-2:
            if i != 0 and nums[i-1] == nums[i]:
                i += 1
                continue

            dic = {}
            for j in range(i+1, n):
                if j != i + 1 and nums[j-1] == nums[j]:
                    continue
                if -nums[j] in dic:
                    ans.append([nums[i], -(nums[i] + nums[j]), nums[j]])
                else:
                    dic[(nums[i] + nums[j])] = 1
            i += 1

        return ans


nums = [-1,0,1,2,-1,-4]
ans = Solution().threeSum(nums)
print(ans)
