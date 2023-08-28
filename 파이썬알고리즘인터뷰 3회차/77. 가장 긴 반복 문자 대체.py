from collections import deque
import string

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        for target_ch in list(string.ascii_uppercase):
            count = k
            st = 0
            q = deque()

            for i, ch in enumerate(s):
                if ch != target_ch:
                    if k != 0:
                        if count == 0:
                            st = q.popleft() + 1
                            count += 1
                        q.append(i)
                        count -= 1
                    else:
                        st = i + 1
                        continue
                ans = max(ans, i - st + 1)
        return ans

s = "ABAB"
k = 2
s = "AABABBA"
k = 1
s = "AAAA"
k = 0
s = "ABAA"
k = 0
ret = Solution().characterReplacement(s,k)
print(ret)