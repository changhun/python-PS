from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        enums = list(enumerate(nums))
        enums.sort(key=lambda x: x[1])
        left, right = 0, len(nums) - 1
        while left < right:
            _sum = enums[left][1] + enums[right][1]
            if _sum == target:
                return [enums[left][0], enums[right][0]]
            elif _sum < target:
                left += 1
            elif _sum > target:
                right -= 1



nums = [2,7,11,15]
target = 9
nums = [3,2,4]
target = 6
ret = Solution().twoSum(nums, target)
print(ret)