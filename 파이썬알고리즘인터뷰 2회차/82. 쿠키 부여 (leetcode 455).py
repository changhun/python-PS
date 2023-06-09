from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ans = 0
        child_index = 0
        g.sort()
        s.sort()
        for value in s:
            if child_index >= len(g):
                break

            if value >= g[child_index]:
                child_index += 1
                ans += 1
        return ans