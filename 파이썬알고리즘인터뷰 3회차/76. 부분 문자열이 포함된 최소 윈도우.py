import collections
INF = int(1e9)

def is_all_not_bigger_then_zero(l):
    for val in l:
        if val > 0:
            return False
    return True

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts = collections.Counter(t)
        st = 0
        min_win_st = 0
        min_win_end = INF
        for i in range(len(s)):
            ch = s[i]
            if ch in counts:
                counts[ch] -= 1
                if counts[ch] <= 0 and is_all_not_bigger_then_zero(counts.values()):
                    while st < i:
                        if s[st] in counts and counts[s[st]] == 0:
                            break
                        if s[st] in counts:
                            counts[s[st]] += 1
                        st += 1

                    if i - st + 1 < min_win_end - min_win_st + 1:
                        min_win_end, min_win_st = i, st

        if min_win_end == INF:
            return ""
        return s[min_win_st:min_win_end+1]


s = "ADOBECODEBANC"
t = "ABC"
s = "a"
t = "a"
ret = Solution().minWindow(s, t)
print(ret)
