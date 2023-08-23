from typing import List
import bisect

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)-1):
            j = bisect.bisect_left(numbers, target - numbers[i], i+1)
            if i < j < len(numbers) and numbers[j] == target - numbers[i]:
                return [i+1, j+1]
        return [0, 0]

numbers = [2,7,11,15]
target = 9
numbers = [2,3,4]
target = 6
numbers = [-1,0]
target = -1
ret = Solution().twoSum(numbers, target)
print(ret)