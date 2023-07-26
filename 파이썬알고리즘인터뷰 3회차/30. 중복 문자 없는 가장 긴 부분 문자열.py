import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        st = 0
        ans = 0
        for i, ch in enumerate(s):

            if ch in dic:
                pos = dic[ch]
                while st <= pos:
                    del dic[s[st]]
                    st += 1

            ans = max(ans, i - st + 1)
            dic[ch] = i

        return ans


s = "abcabcbb"
ret = Solution().lengthOfLongestSubstring(s)
print(ret)

