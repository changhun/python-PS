from typing import List
import bisect

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers[:-1]):
            ret = bisect.bisect_left(numbers, target - num, i + 1)
            if ret < len(numbers) and numbers[ret] == target - num:
                return [i + 1, ret + 1]
