import collections

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        count = collections.Counter(stones)
        for ch in jewels:
            ans += count[ch]
        return ans


jewels = "aA"
stones = "aAAbbbb"
jewels = "z"
stones = "ZZ"
ret = Solution().numJewelsInStones(jewels, stones)
print(ret)