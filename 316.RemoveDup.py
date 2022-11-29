import collections
import re


class Solution:


    def removeDup(self, s:str) -> str:
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            if (set(s) == set(suffix)):
                return char + self.removeDup(suffix.replace(char, ''))

        return ''

sol = Solution()
s = "cbacdcbc"
print(sol.removeDup(s))