class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        max_len = 0

        for i in range(len(s)):
            left = right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            left += 1
            right -= 1
            if right - left + 1 > max_len:
                max_len = right - left + 1
                ans = s[left:right+1]

        for i in range(len(s) - 1):
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            left += 1
            right -= 1
            if right - left + 1 > max_len:
                max_len = right - left + 1
                ans = s[left:right + 1]

        return ans

s = "babad"
s = "cbbd"
s = "babad"
ret = Solution().longestPalindrome(s)
print(ret)