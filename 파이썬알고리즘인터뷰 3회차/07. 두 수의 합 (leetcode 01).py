from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_pairs = [(num, i) for i, num in enumerate(nums)]
        num_pairs.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            if num_pairs[left][0] + num_pairs[right][0] == target:
                return [num_pairs[left][1], num_pairs[right][1]]
            elif num_pairs[left][0] + num_pairs[right][0] < target:
                left += 1
            else:
                right -= 1


nums = [2,7,11,15]
target = 9
nums = [3,2,4]
target = 6
ret = Solution().twoSum(nums, target)
print(ret)
