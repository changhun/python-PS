from typing import List

""" ver1 """
#"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_k(s, e):
            for i in range(len(nums) - 1):
                if nums[i+1] < nums[i]:
                    return i+1;
            return 0; # no pivot

        def binary_search(s, e):
            while s <= e:
                m = s + (e - s) // 2
                if nums[m] < target:
                    s = m + 1
                elif nums[m] > target:
                    e = m - 1
                else:
                    return m
            return -1

        k = find_k(0, len(nums) - 1)
        ret1 = binary_search(0, k - 1)
        ret2 = binary_search(k, len(nums) - 1)
        if ret1 != -1:
            return ret1
        elif ret2 != -1:
            return ret2
        return -1
#"""

""" ver2 modify find_k to find k in log(n) """
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_k(s, e):
            for i in range(len(nums) - 1):
                if nums[i+1] < nums[i]:
                    return i+1;
            return 0; # no pivot

        def binary_search(s, e):
            while s <= e:
                m = s + (e - s) // 2
                if nums[m] < target:
                    s = m + 1
                elif nums[m] > target:
                    e = m - 1
                else:
                    return m
            return -1

        k = find_k(0, len(nums) - 1)
        ret1 = binary_search(0, k - 1)
        ret2 = binary_search(k, len(nums) - 1)
        if ret1 != -1:
            return ret1
        elif ret2 != -1:
            return ret2
        return -1
"""

""" ver3 """
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def search_in_circular(s, e):
            if s > e:
                return -1

            m = s + (e - s)//2
            if nums[m] == target:
                return m

            if nums[s] <= nums[m]:
                if target <= nums[m]:
                    return binary_search(s, m)
                else:
                    return search_in_circular(m+1, e)
            else:
                if target <= nums[m]:
                    return search_in_circular(s, m)
                else:
                    return binary_search(m+1, e)

        def binary_search(s, e):
            while s <= e:
                m = s + (e - s) // 2
                if nums[m] < target:
                    s = m + 1
                elif nums[m] > target:
                    e = m - 1
                else:
                    return m
            return -1
"""

nums = [4,5,6,7,0,1,2]
target = 0
ret = Solution().search(nums, target)
print(ret)
