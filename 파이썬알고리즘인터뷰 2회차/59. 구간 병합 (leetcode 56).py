from typing import List
from functools import cmp_to_key

def comparator_by_elemenets(a, b):
    if a[0] > b[0] or (a[0] == b[0] and a[1] > b[1]):
        return 1
    elif a[0] == b[0] and a[1] == b[1]:
        return 0
    else:
        return -1


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key=cmp_to_key(comparator_by_elemenets))
        #intervals.sort(key=lambda x : (x[0], x[1]))
        #intervals.sort()
        ans = [[intervals[0][0], intervals[0][1]]]
        for s, e in intervals[1:]:
            if s <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], e)
            else:
                ans.append([s, e])

        return ans



intervals = [[1,4],[4,5]]
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
ret = Solution().merge(intervals)
print(ret)