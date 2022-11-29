import collections


class Solution:
    def longestPalindrome(self, s: str) -> str:

        #def odd_palindrome(mid: int, ans):
        def odd_palindrome(mid: int):
            left = right = mid

            while 0 <= left - 1 and right + 1 <= len(s)-1 and s[left-1] == s[right+1]:
                left -= 1
                right += 1
            '''
            if right - left + 1 > len(ans):
                ans = s[left:right+1]
             '''
            if right - left + 1 > len(ans):
                return s[left:right+1]
            return ans


        def even_palindrome(mid: int):
            left = mid
            right = mid + 1
            if (s[left] != s[right]):
                return ans

            while 0 <= left - 1 and right + 1 <= len(s)-1 and s[left-1] == s[right+1]:
                left -= 1
                right += 1

            if right - left + 1 > len(ans):
                return s[left:right + 1]
            return ans

        ans = []
        for i in range(len(s)):
            ans = odd_palindrome(i)

        for i in range(len(s) - 1):
            ans = even_palindrome(i)

        print(''.join(ans))
        return ''.join(ans)


sol = Solution()

sol.longestPalindrome("cbbd")