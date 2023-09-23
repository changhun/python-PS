class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans_s = ans_e = 0
        s_len = len(s)

        for i in range(1, s_len):
            cur_s = cur_e = i
            while cur_s - 1 >= 0 and cur_e + 1 < s_len and s[cur_s - 1] == s[cur_e + 1]:
                cur_s -= 1
                cur_e += 1
            if cur_e - cur_s > ans_e - ans_s:
                ans_e = cur_e
                ans_s = cur_s

        for i in range(0, s_len - 1):
            cur_s = i
            cur_e = i + 1
            if s[cur_s] != s[cur_e]:
                continue
            while cur_s - 1 >= 0 and cur_e + 1 < s_len and s[cur_s - 1] == s[cur_e + 1]:
                cur_s -= 1
                cur_e += 1
            if cur_e - cur_s > ans_e - ans_s:
                ans_s = cur_s
                ans_e = cur_e
        return s[ans_s:ans_e+1]


s = "babad"
s = "cbbd"
ret = Solution().longestPalindrome(s)
print(ret)