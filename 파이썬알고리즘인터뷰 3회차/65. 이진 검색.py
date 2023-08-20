from typing import List

"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums) - 1

        while s <= e:
            m = (s + e)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                s = m + 1
            else:
                e = m - 1
        return -1
"""

""" sol 2: bisect """
import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pos = bisect.bisect_left(nums, target)
        if pos < len(nums) and nums[pos] == target:
            return pos
        return -1

