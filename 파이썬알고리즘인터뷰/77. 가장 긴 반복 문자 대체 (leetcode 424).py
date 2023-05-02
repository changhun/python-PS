import collections
from string import ascii_uppercase
import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        counter = collections.Counter(s)

        #for char in ascii_uppercase:
        for char in counter.keys():
            remain_k = k
            st = 0
            for cur in range(len(s)):
                if s[cur] != char:
                    while remain_k <= 0:
                        if s[st] != char:
                            remain_k += 1
                        st += 1

                    remain_k -= 1

                ans = max(ans, cur - st + 1)
        return ans

s = "ABAB"
k = 2
s = "AABABBA"
k = 1
ret = Solution().characterReplacement(s, k)
print(ret)