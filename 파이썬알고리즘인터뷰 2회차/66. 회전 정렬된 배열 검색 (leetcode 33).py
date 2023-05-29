from typing import List
import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_pivot(s, e):
            if s >= e or nums[s] < nums[e]:
                return -1
            m = (s + e + 1) // 2
            if m > 0 and nums[m-1] > nums[m]:
                return m
            if nums[s] > nums[m-1]:
                return find_pivot(s, m-1)
            else:
                #return find_pivot(m+1, e)
                return find_pivot(m, e)

        pivot = find_pivot(0, len(nums) - 1)
        if pivot == -1:
            ret = bisect.bisect_left(nums, target, 0, len(nums) - 1)
            if ret < len(nums) and nums[ret] == target:
                return ret
            return -1
        else:
            if nums[0] <= target <= nums[pivot - 1]:
                ret = bisect.bisect_left(nums, target, 0, pivot - 1)
                if ret < pivot and nums[ret] == target:
                    return ret
                return -1
            elif nums[pivot] <= target <= nums[len(nums) - 1]:
                ret = bisect.bisect_left(nums, target, pivot, len(nums) - 1)
                if ret < len(nums) and nums[ret] == target:
                    return ret
                return -1
            else:
                return -1


nums = [4,5,6,7,0,1,2]
target = 0
nums = [3, 1]
target = 1
ret = Solution().search(nums, target)
print(ret)