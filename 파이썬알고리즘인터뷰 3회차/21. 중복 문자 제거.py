import collections
from collections import deque

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        l = deque()
        ans = []
        count = collections.Counter(s)
        processed = {}
        for ch in s:
            if ch in processed:
                continue

            if ch in l:
                if count[ch] == 1:
                    while l and l[0] <= ch:
                        ans.append(l[0])
                        processed[l[0]] = 1
                        l.popleft()
                count[ch] -= 1
                continue

            while l and l[-1] >= ch:
                l.pop()
            l.append(ch)
            count[ch] -= 1
            if count[ch] == 0:
                ans += l
                for val in l:
                    processed[val] = 1
                l = deque()

        return ''.join(ans)


s = "bcabc"
s = "cbacdcbc"
s = "abacb"
s = "bddbccd"
ret = Solution().removeDuplicateLetters(s)
print(ret)