from typing import List
from functools import cmp_to_key

# 1. sort 에 comparator 사용
#    - cmp_to_key
# 2. 문자열 compare
#    - 재귀
# 3. 알맞은 포맷으로 리턴
#    - return str(int(ret))
#      "00"  같은 값 알맞은 포맷으로 변경 => "0"

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def comp(a, b):
            len1 = len(a)
            len2 = len(b)
            min_len = min(len1, len2)

            for i in range(min(len1, len2)):
                if a[i] < b[i]:
                    return -1
                elif a[i] > b[i]:
                    return 1

            if len1 == len2:
                return 0
            elif len1 > len2:
                return comp(a[min_len:], b)
            else:
                return comp(a, b[min_len:])


        str_nums = [str(num) for num in nums]
        # str_nums.reverse(key=comp)
        #str_nums.sort(key=comp)
        str_nums.sort(key=cmp_to_key(comp))
        print(str_nums)
        str_nums.reverse()
        ret = ''.join(str_nums)
        return str(int(ret))

nums = [10,2]
nums = [3,30,34,5,9]
ret = Solution().largestNumber(nums)
print(ret)


""""""
"""
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def comp(a, b):
            len1 = len(a)
            len2 = len(b)
            min_len = min(len1, len2)

            for i in range(min(len1, len2)):
                if a[i] < b[i]:
                    return -1
                elif a[i] > b[i]:
                    return 1

            if len1 == len2:
                return 0
            elif len1 > len2:
                for i in range(min_len, len1):
                    if a[i] < b[0]:
                        return -1
                    elif a[i] > b[0]:
                        return 1
                return 0

            elif len1 < len2:
                for i in range(min_len, len2):
                    if a[0] < b[i]:
                        return -1
                    elif a[0] > b[i]:
                        return 1
                return 0

        str_nums = [str(num) for num in nums]
        # str_nums.reverse(key=comp)
        #str_nums.sort(key=comp)
        str_nums.sort(key=cmp_to_key(comp))
        print(str_nums)
        str_nums.reverse()
        ret = ''.join(str_nums)
        return ret
"""


nums = [10,2]
nums = [3,30,34,5,9]
nums = [432,43243]
ret = Solution().largestNumber(nums)
print(ret)


