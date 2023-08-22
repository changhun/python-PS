from typing import List
import bisect


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        ans = []
        cur = nums1[0]
        pos = bisect.bisect_left(nums2, cur)
        if pos < len(nums2) and nums2[pos] == cur:
            ans.append(cur)

        for idx in range(1, len(nums1)):
            if nums1[idx - 1] == nums1[idx]:
                continue
            pos = bisect.bisect_left(nums2, nums1[idx])
            if pos < len(nums2) and nums2[pos] == nums1[idx]:
                ans.append(nums1[idx])
        return ans


nums1 = [1,2,2,1]
nums2 = [2, 2]
ret = Solution().intersection(nums1, nums2)
print(ret)
