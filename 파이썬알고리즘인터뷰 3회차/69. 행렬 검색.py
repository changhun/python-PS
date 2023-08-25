from typing import List
import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        e = m
        for i in range(n):
            e = bisect.bisect_left(matrix[i], target, 0, e)
            if e < m and matrix[i][e] == target:
                return True
        return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
ret = Solution().searchMatrix(matrix, target)
print(ret)


