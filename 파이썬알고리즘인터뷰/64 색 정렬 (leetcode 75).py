from typing import List

""" sol1 : insertion sort """
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(1, len(nums)):
            for j in range(i, 0, -1):
                if nums[j-1] <= nums[j]:
                    break

                nums[j-1], nums[j] = nums[j], nums[j-1]
"""


""" sol2 """
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = [0]*3
        for num in nums:
            counts[num] +=1

        i = 0
        for num in range(3):
            for _ in range(counts[num]):
                nums[i] = num
                i += 1

nums = [2,0,2,1,1,0]
Solution().sortColors(nums)
print(nums)