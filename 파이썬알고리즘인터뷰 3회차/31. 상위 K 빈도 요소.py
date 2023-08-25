import collections

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return [item[0] for item in collections.Counter(nums).most_common(k)]


nums = [1,1,1,2,2,3]
k = 2
ret = Solution().topKFrequent(nums, k)
print(ret)
