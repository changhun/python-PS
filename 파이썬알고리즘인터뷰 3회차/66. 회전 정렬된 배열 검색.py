from typing import List
import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_pivot(s, e):
            if s == e or nums[s] <= nums[e]:
                return -1
            m = (s+e)//2
            if nums[m] > nums[m+1]:
                return m
            ret = find_pivot(s, m)
            if ret != -1:
                return ret
            ret = find_pivot(m+1, e)
            return ret

        pivot = find_pivot(0, len(nums)-1)

        if pivot != -1:
            sorted = nums[pivot+1:] + nums[:pivot+1]
        else:
            sorted = nums
        ans = bisect.bisect_left(sorted, target)
        if not (ans < len(nums) and sorted[ans] == target):
            ans = -1

        if ans != -1:
            len_pivot = len(nums) - pivot - 1
            ans = (ans + len(nums) - len_pivot) % len(nums)
        return ans


nums = [4,5,6,7,0,1,2]
target = 0
ret = Solution().search(nums, target)
print(ret)
