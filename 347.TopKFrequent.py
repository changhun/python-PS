import collections
import heapq


class Solution:

    '''ver1
    def topKfrequent(self, nums:list[int], k:int)->list[int]:
        freqs = collections.Counter(nums)
        heap_freqs = []
        for f in freqs:
            heapq.heappush(heap_freqs, (-freqs[f], f))

        topK = []
        for _ in range(k):
            topK.append(heapq.heappop(heap_freqs)[1])

        return topK
    '''

    #'''ver2
    def topKfrequent(self, nums: list[int], k: int) -> list[int]:
        heap = []
        freqs = collections.Counter(nums)

        topK = []
        for f in freqs.most_common(k):
            topK.append(f[0])

        return topK
    #'''

sol = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = 2

print(sol.topKfrequent(nums, k))