import collections
import sys
INF = sys.maxsize

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_window_include_str(window, counter):
            for char, count in counter.items():
                if window[char] < count:
                    return False
            return True

        window = collections.defaultdict(int)
        counter = collections.Counter(t)
        st = 0
        s_len = len(s)
        ans_s = 0
        ans_e = INF
        for e, char in enumerate(s):
            window[char] += 1
            if char in counter:
                ret = is_window_include_str(window, counter)
                if ret is False:
                    continue
                if e - st < ans_e - ans_s:
                    ans_s, ans_e = st, e

                while st <= e:
                    tmp_char = s[st]
                    window[tmp_char] -= 1
                    st += 1
                    if tmp_char in counter and window[tmp_char] < counter[tmp_char]:
                        break
                    if e - st < ans_e - ans_s:
                        ans_s, ans_e = st, e

        #print(ans_s, ans_e)
        if ans_e == INF:
            return ""
        return s[ans_s: ans_e + 1]


s = "ADOBECODEBANC"
t = "ABC"
ret = Solution().minWindow(s, t)
print(ret)