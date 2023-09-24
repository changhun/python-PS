from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            if target - num in dic:
                return [i, dic[target - num]]
            dic[num] = i


nums = [2,7,11,15]
target = 9
nums = [3,2,4]
target = 6
ret = Solution().twoSum(nums, target)
print(ret)
