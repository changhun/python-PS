import collections
INF = int(1e9)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts = collections.Counter(s)
        st = 0
        min_win_st = 0
        min_win_end = INF
        for i in range(len(s)):
            ch = s[i]
            if ch in counts:
                counts[ch] -= 1
                if counts[ch] < 0:
                    is_t_included = True
                    for count in counts.values():
                        if count > 0:
                            is_t_included = False
                            break

