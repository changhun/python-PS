class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        start = cur = 0
        ans = 0
        cur_len = 0
        for c in s:
            if c in d:
                while s[start] != c:
                    del d[s[start]]
                    start += 1
                    cur_len -= 1

                del d[s[start]]
                start += 1
                cur_len -= 1

            cur_len += 1
            d[c] = 1
            ans = max(ans, cur_len)
        return ans

s = "abcabcbb"
ret = Solution().lengthOfLongestSubstring(s)
print(ret)
