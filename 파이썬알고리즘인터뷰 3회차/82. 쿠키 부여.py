from typing import List
import bisect

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0
        si = 0
        for greed in g:
            target_pos = bisect.bisect_left(s, greed, si)
            if target_pos == len(s):
                return ans

            if target_pos < len(s):
                ans += 1
                si = target_pos + 1
        return ans
