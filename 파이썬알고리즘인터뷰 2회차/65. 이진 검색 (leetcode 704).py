from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums) - 1

        while s <= e:
            m = (s + e) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                s = m + 1
            else:
                e = m - 1

        return -1


""" sol2: recursive """
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(s, e):
            if s > e:
                return -1
            m = (s + e)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                return binarySearch(m + 1, e)
            else:
                return binarySearch(s, m - 1)
        return binarySearch(0, len(nums)-1)


""" sol3: using bisect """
import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ret = bisect.bisect_left(nums, target, 0, len(nums)-1)
        if ret >= len(nums) or nums[ret] != target:
            return -1
        return ret