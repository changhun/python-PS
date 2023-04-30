from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        prev = intervals[0]
        for interval in intervals[1:]:
            if interval[0] <= prev[1]:
                if prev[1] < interval[1]:
                    prev[1] = interval[1]
            else:
                ans.append(prev)
                prev = interval
        ans.append(prev)
        return ans