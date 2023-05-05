from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        satisfied_count = 0
        child_num = len(g)
        for cookie in s:
            if g[satisfied_count] <= cookie:
                satisfied_count += 1
                if satisfied_count >= child_num:
                    break

        return satisfied_count


g = [1,2]
s = [1,2,3]
ret = Solution().findContentChildren(g, s)
print(ret)