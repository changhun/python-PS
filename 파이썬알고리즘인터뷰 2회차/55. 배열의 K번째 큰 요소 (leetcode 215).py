from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = [-num for num in nums]
        heapq.heapify(hq)

        for i in range(k):
            ret = heapq.heappop(hq)

        return -ret
