from typing import List
import heapq
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        ans = []
        counts = collections.defaultdict(int)

        for i in range(k):
            counts[nums[i]] += 1
            heapq.heappush(max_heap, -nums[i])

        ans.append(-max_heap[0])

        for i in range(k, len(nums)):
            counts[nums[i - k]] -= 1
            counts[nums[i]] += 1
            heapq.heappush(max_heap, -nums[i])

            while not counts[-max_heap[0]]:
                heapq.heappop(max_heap)
            ans.append(-max_heap[0])
        return ans


nums = [1,3,-1,-3,5,3,6,7]
k = 3
ret = Solution().maxSlidingWindow(nums, k)
print(ret)