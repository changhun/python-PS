from typing import List
import bisect


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search_matrix(row, col_end):
            if row >= len(matrix) or col_end < 0:
                return False

            i = bisect.bisect_left(matrix[row], target, 0, col_end)
            if i < col_end and matrix[row][i] == target:
                return True

            return search_matrix(row + 1, i)

        ret = search_matrix(0, len(matrix[0]))
        return ret

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
matrix = [[5],[6]]
target = 6

ret = Solution().searchMatrix(matrix, target)
print(ret)

nums = [5]
ret = bisect.bisect_left(nums, 6,)
print(ret)