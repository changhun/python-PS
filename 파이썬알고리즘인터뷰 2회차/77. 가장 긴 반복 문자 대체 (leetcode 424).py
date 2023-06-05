from collections import deque

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def get_consequent_len(char, k):
            n = len(s)
            st = 0
            q = deque()
            ans = 0
            for e in range(n):
                if s[e] != char:
                    ans = max(ans, e - st)
                    if k == 0:
                        if q:
                            st = q.popleft() + 1
                            q.append(e)
                        else:
                            st = e + 1
                    else:
                        k -= 1
                        q.append(e)

            ans = max(ans, n - st)
            return ans

        ret = 0
        alphas = [chr(c) for c in range(ord('A'), ord('Z') + 1)]
        for char in alphas:
            ret = max(ret, get_consequent_len(char, k))
        return ret


s = "ABAB"
k = 2
s = "AABABBA"
k = 1
s = "AAAA"
k = 0
ret = Solution().characterReplacement(s, k)
print(ret)