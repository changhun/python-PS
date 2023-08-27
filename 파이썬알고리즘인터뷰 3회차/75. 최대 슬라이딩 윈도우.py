from typing import List
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        hp = []
        for i in range(k-1):
            heapq.heappush(hp, (-nums[i], i))

        s = 0
        ans = []
        for i in range(k-1, len(nums)):
            heapq.heappush(hp, (-nums[i], i))
            while hp[0][1] < s:
                heapq.heappop(hp)
            max_val = -hp[0][0]
            ans.append(max_val)
            s += 1
        return ans

nums = [1,3,-1,-3,5,3,6,7]
k = 3
ret = Solution().maxSlidingWindow(nums, k)
print(ret)