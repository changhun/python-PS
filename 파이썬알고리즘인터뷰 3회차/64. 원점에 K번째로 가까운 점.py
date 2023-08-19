from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda x: x[0]*x[0] + x[1]*x[1])[:k]


points = [[1,3],[-2,2]]
k = 1
points = [[3,3],[5,-1],[-2,4]]
k = 2
ret = Solution().kClosest(points, k)
print(ret)