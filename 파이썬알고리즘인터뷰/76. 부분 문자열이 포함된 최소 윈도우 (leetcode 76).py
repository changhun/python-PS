import sys
import collections

"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_len = sys.maxsize
        st, cur = 0, 0
        dic = collections.defaultdict(int)
        def is_window_contain_t():
            for val in dic.values():
                if val > 0:
                    return False
            return True

        for char in t:
            dic[char] += 1

        st = 0
        ans_pos = 0
        for cur in range(len(s)):
            if s[cur] in dic:
                dic[s[cur]] -= 1

            if is_window_contain_t():
                while s[st] not in dic or dic[s[st]] < 0:
                    if s[st] in dic:
                        dic[s[st]] += 1
                    st += 1

                if cur - st + 1 < min_len:
                    min_len = cur - st + 1
                    ans_pos = st
        if min_len == sys.maxsize:
            min_len = 0
        return s[ans_pos:ans_pos + min_len]
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_len = sys.maxsize
        st, cur = 0, 0
        dic = collections.defaultdict(int)
        def is_window_contain_t():
            for val in dic.values():
                if val > 0:
                    return False
            return True

        for char in t:
            dic[char] += 1

        st = 0
        ans_pos = 0
        for cur in range(len(s)):
            dic[s[cur]] -= 1

            if is_window_contain_t():
                while dic[s[st]] < 0:
                    dic[s[st]] += 1
                    st += 1

                if cur - st + 1 < min_len:
                    min_len = cur - st + 1
                    ans_pos = st
        if min_len == sys.maxsize:
            min_len = 0
        return s[ans_pos:ans_pos + min_len]



s = "a"
t = "a"
s = "a"
t = "aa"
s = "ADOBECODEBANC"
t = "ABC"
ret = Solution().minWindow(s, t)
print(ret)
