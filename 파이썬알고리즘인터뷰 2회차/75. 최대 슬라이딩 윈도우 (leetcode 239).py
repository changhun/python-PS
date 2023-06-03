from typing import List
import heapq
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        ans = []
        counter = collections.defaultdict(int)
        for num in nums[:k-1]:
            heapq.heappush(heap, -num)
            counter[num] += 1

        nums_length = len(nums)
        for i in range(k-1, nums_length):
            heapq.heappush(heap, -nums[i])
            counter[nums[i]] += 1
            while counter[-heap[0]] == 0:
                heapq.heappop(heap)

            ans.append(-heap[0])
            counter[nums[i-(k-1)]] -= 1
        return ans


nums = [1,3,-1,-3,5,3,6,7]
k = 3
nums = [1]
k = 1

ret = Solution().maxSlidingWindow(nums, k)
print(ret)