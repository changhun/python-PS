from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        cur = intervals[0]
        for interval in intervals[1:]:
            if cur[1] >= interval[0]:
                cur[1] = max(cur[1], interval[1])
            else:
                ans.append(cur[:])
                cur = interval
        ans.append(cur[:])
        return ans


intervals = [[1,3],[2,6],[8,10],[15,18]]

ret = Solution().merge(intervals)
print(ret)