from typing import List

""" sol1: using dictinoary """
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums_length = len(nums)
        dic = {}
        ans = set()
        for second in range(1, nums_length-1):
            dic[nums[second - 1]] = second - 1
            for third in range(second + 1, nums_length):
                if -(nums[second] + nums[third]) in dic:
                    ans.add((- (nums[second] + nums[third]), nums[second], nums[third]))

        ret = [list(item) for item in ans]
        return ret
"""

""" sol2: using bisect """
"""
import bisect
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums_length = len(nums)
        ans = set()
        for second in range(1, nums_length-1):
            for third in range(second + 1, nums_length):
                index = bisect.bisect_left(nums, -(nums[second] + nums[third]), 0, second - 1)
                if index < second and nums[index] == -(nums[second] + nums[third]):
                    ans.add((nums[index], nums[second], nums[third]))
        return [list(item) for item in ans]
"""

""" sol3: using two pointer """
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for first in range(len(nums)-2):
            if first > 0 and nums[first-1] == nums[first]:
                continue
            second = first + 1
            third = len(nums) - 1
            while second < third:
                three_sum = nums[first] + nums[second] + nums[third]
                if three_sum == 0:
                    ans.append([nums[first], nums[second], nums[third]])
                    second += 1
                    third -= 1
                    while second < third and nums[second-1] == nums[second]:
                        second += 1
                    while second < third and nums[third] == nums[third+1]:
                        third -= 1
                elif three_sum < 0:
                    second += 1
                    while second < third and nums[second-1] == nums[second]:
                        second += 1
                elif three_sum > 0:
                    third -= 1
                    while second < third and nums[third] == nums[third+1]:
                        third -= 1
        return ans

nums = [-1,0,1,0]
nums = [-1,0,1,2,-1,-4]
nums = [0,1,1]
nums = [-2,0,0,2,2]
ret = Solution().threeSum(nums)
print(ret)