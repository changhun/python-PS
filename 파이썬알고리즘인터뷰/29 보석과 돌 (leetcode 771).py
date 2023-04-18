import collections

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = collections.Counter(stones)
        ans = 0
        for c in jewels:
            #if c in counter:
            #    ans += counter[c]
            ans += counter[c]
        return ans
