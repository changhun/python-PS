from typing import List
import bisect

"""    
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        ans = []
        for i, num in enumerate(nums1):
            if i == 0 or nums1[i-1] != nums1[i]:
                index = bisect.bisect_left(nums2, num)
                if index < len(nums2) and nums2[index] == num:
                    ans.append(num)
        return ans
"""

#""" Sol2: using set and intersection()
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set()
        s1 = set(nums1)
        s2 = set(nums2)
        ans = s1.intersection(s2)
        #print(ans)
        #print(type(ans))
        return list(ans)
#"""

nums1 = [1,2,2,1]
nums2 = [2,2]
ret = Solution().intersection(nums1, nums2)
print(ret)

