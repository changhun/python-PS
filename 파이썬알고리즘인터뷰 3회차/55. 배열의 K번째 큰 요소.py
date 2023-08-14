from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = [-num for num in nums]
        heapq.heapify(hq)
        for _ in range(k):
            num = -heapq.heappop(hq)
        return num
