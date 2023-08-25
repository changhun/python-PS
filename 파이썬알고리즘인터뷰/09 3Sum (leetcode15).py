
""" two pointer"""
def threeSum(nums: list[int]) -> list[list[int]]:
    answer = []
    nums.sort()
    n = len(nums)
    for i in range(n-2):
        complement = -nums[i]
        lo, hi = i+1, n-1
        while lo < hi:
            if nums[lo] + nums[hi] == complement:
                if [nums[i], nums[lo], nums[hi]] not in answer:
                    answer.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
            elif nums[lo] + nums[hi] < complement:
                lo += 1
            elif nums[lo] + nums[hi] > complement:
                hi -= 1
    return answer

""" Dictionary """


""" Binary Search """


nums = [0,1,1]
nums = [0,0,0]
nums = [-1,0,1,2,-1,-4]
ret = threeSum(nums)
print(ret)