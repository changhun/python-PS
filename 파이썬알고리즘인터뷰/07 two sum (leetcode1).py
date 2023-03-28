import collections

""" solution using collections.Counter
def twoSum(nums: list[int], target):
    dic = collections.Counter(nums)
    #for i in range(len(nums)):
    for i in range(len(nums)-1, -1, -1):
        other_value = target - nums[i]
        if other_value in dic and (nums[i] != other_value or dic[other_value] >= 2):
            return [i, nums.index(target - nums[i])]
            # return list((i, nums.index(target - nums[i])))
"""

""" using dict() """

""" using two pointer """
def twoSum(nums: list[int], target):
    sorted_nums = [(nums[i], i) for i in range(len(nums))]
    sorted_nums.sort()
    #sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])

    lo = 0
    hi = len(sorted_nums) - 1
    while lo < hi:
        if sorted_nums[lo][0] + sorted_nums[hi][0] == target:
            return [sorted_nums[lo][1], sorted_nums[hi][1]]
        elif sorted_nums[lo][0] + sorted_nums[hi][0] > target:
            hi -= 1
        elif sorted_nums[lo][0] + sorted_nums[hi][0] < target:
            lo += 1


nums = [2,7,11,15]
target = 9

nums = [3,2,4]
target = 6
ret = twoSum(nums, target)
print(ret)