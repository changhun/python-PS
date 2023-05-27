from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def my_comparator(a: str, b: str):
            if a + b > b + a:
                return -1
            elif a + b == b + a:
                return 0
            else:
                return 1

        str_nums = [str(num) for num in nums]
        str_nums.sort(key=cmp_to_key(my_comparator))
        ret = ''.join(str_nums)
        if int(ret) == 0:
            return "0"
        return ret


nums = [3,30,34,5,9]
ret = Solution().largestNumber(nums)
print(ret)
