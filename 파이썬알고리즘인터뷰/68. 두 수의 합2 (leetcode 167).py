from typing import List
import bisect

"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 1):
            ret = bisect.bisect_left(numbers[i+1:], target - numbers[i])
            if i + 1 + ret < len(numbers) and numbers[i + 1 + ret] == target - numbers[i]:
                return [i + 1, i + ret + 1 + 1]
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 1):
            ret = bisect.bisect_left(numbers, target - numbers[i], i + 1)
            if ret < len(numbers) and numbers[ret] == target - numbers[i]:
                return [i + 1, ret + 1]



numbers = [2,7,11,15]
target = 9
numbers = [5,25,75]
target = 100
ret = Solution().twoSum(numbers, target)
print(ret)

