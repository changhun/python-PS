import collections
from typing import List
import bisect
import sys
from collections import defaultdict

""" sol1: binary search"""
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        nums1.sort()
        nums2.sort()
        prev = -sys.maxsize
        for num in nums2:
            if num == prev:
                continue
            prev = num

            index = bisect.bisect_left(nums1, num)
            if index < len(nums1) and nums1[index] == num:
                ans.append(num)
        return ans
"""

""" sol2: hash """
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        dict = collections.defaultdict(int)
        for num in nums1:
            dict[num] += 1

        nums2.sort()
        prev = -sys.maxsize
        for num in nums2:
            if prev == num:
                continue
            prev = num

            if num in dict:
                ans.append(num)
        return ans
"""

""" sol3: set """
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        ans = []
        for num in nums2_set:
            if num in nums1_set:
                ans.append(num)

        return ans